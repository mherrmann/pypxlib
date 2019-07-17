from collections import OrderedDict
from datetime import date, time, datetime
from os.path import isfile
from pypxlib.pxlib_ctypes import *

import atexit

PX_boot()
atexit.register(PX_shutdown)

class Table(object):

	PX_ENCODING = 'ascii'

	class Iterator(object):
		def __init__(self, table):
			self.table = table
			self.i = 0
		def next(self):
			if self.i < len(self.table):
				result = self.table[self.i]
				self.i += 1
				return result
			raise StopIteration()
		# Python 3:
		__next__ = next

	def __init__(self, file_path, encoding='cp850', blob_file_path=None):
		if not blob_file_path:
			possible_blob_file = \
				file_path.replace('.db', '.mb').replace('.DB', '.MB')
			if isfile(possible_blob_file):
				blob_file_path = possible_blob_file
		self.file_path = file_path
		self.encoding = encoding
		self.pxdoc = PX_new()
		if PX_open_file(self.pxdoc, file_path.encode(self.PX_ENCODING)) != 0:
			raise PXError('Could not open file %s.' % self.file_path)
		if blob_file_path:
			blob_file_path_enc = blob_file_path.encode(self.PX_ENCODING)
			if PX_set_blob_file(self.pxdoc, blob_file_path_enc) < 0:
				raise PXError('Could not open BLOB file %s.' % blob_file_path)
		self._fields_cached = None
	def __enter__(self):
		return self
	@property
	def fields(self):
		if self._fields_cached is None:
			self._fields_cached = OrderedDict()
			num_fields = self.pxdoc.contents.px_head.contents.px_numfields
			for i in range(num_fields):
				field = PX_get_field(self.pxdoc, i).contents
				field_name = field.px_fname.data.decode(self.PX_ENCODING)
				self._fields_cached[field_name] = \
					Field.from_type(ord(field.px_ftype), i, self.encoding)
		return self._fields_cached
	def __getitem__(self, rownum):
		self._check_rownum(rownum)
		_len = len(self)
		if rownum < 0:
			rownum %= _len
		elif rownum > _len:
			raise IndexError('table index out of range.')
		pxvals = PX_retrieve_record(self.pxdoc, rownum)
		if not pxvals:
			raise PXError(
				'Could not retrieve row %d of file %s.' %
				(rownum, self.file_path)
			)
		return Row(self, rownum, pxvals)
	def _check_rownum(self, rownum):
		if not isinstance(rownum, int):
			raise TypeError(
				'Table indices must be integers, not %s.' % type(rownum)
			)
	def __delitem__(self, rownum):
		self._check_rownum(rownum)
		if PX_delete_record(self.pxdoc, rownum) == -1:
			raise PXError(
				'Could not delete row %d of file %s.' %
				(rownum, self.file_path)
			)
	def __len__(self):
		return self.pxdoc.contents.px_head.contents.px_numrecords
	def __iter__(self):
		return Table.Iterator(self)
	def __exit__(self, *_):
		self.close()
	def insert(self, row_tpl):
		if len(row_tpl) != len(self.fields):
			raise ValueError('Wrong number of fields.')
		dataptr = (POINTER(px_val) * len(row_tpl))()
		for i, field in enumerate(self.fields.values()):
			pxval = px_val()
			pxval.type = field.type
			field.serialize_to(row_tpl[i], pxval)
			dataptr[i] = pointer(pxval)
		result = PX_insert_record(self.pxdoc, dataptr)
		if result == -1:
			raise PXError('Could not insert row.')
		return result
	def close(self):
		PX_close(self.pxdoc)
		PX_delete(self.pxdoc)
		self._fields_cached = None
	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__, self.file_path)
	def __str__(self):
		return repr(self)

class Field(object):
	@classmethod
	def from_type(cls, type_, index, encoding):
		if type_ == pxfAlpha:
			return AlphaField(index, type_, encoding)
		if type_ == pxfDate:
			return DateField(index, type_)
		if type_ in (pxfShort, pxfLong, pxfAutoInc):
			return LongField(index, type_)
		if type_ in (pxfNumber, pxfCurrency):
			return DoubleField(index, type_)
		if type_ == pxfLogical:
			return LogicalField(index, type_)
		if type_ in (pxfBLOb, pxfMemoBLOb, pxfBCD, pxfBytes):
			return BytesField(index, type_)
		if type_ in (pxfOLE, pxfGraphic):
			return BytesField(index, type_)
		if type_ == pxfTime:
			return TimeField(index, type_)
		if type_ == pxfTimestamp:
			return TimestampField(index, type_)
		raise PXError('Unrecognized data type: %r' % type_)
	def __init__(self, index, type_):
		self.index = index;
		self.type = type_
	def deserialize(self, pxval):
		if pxval.isnull == b'\x01':
			return None
		return self._deserialize(pxval.value)
	def serialize_to(self, value, pxval):
		if value is None:
			pxval.isnull = b'\x01'
		else:
			pxval.isnull = b'\x00'
			self._serialize_to(value, pxval.value)
	def _deserialize(self, pxval_value):
		raise NotImplementedError()
	def _serialize_to(self, value, pxval_value):
		raise NotImplementedError()

class AlphaField(Field):
	def __init__(self, index, type_, encoding):
		super(AlphaField, self).__init__(index, type_)
		self.encoding = encoding
	def _deserialize(self, pxval_value):
		return pxval_value.str.val.data.decode(self.encoding)
	def _serialize_to(self, value, pxval_value):
		value_enc = value.encode(self.encoding)
		pxval_value.str.val.data = value_enc
		pxval_value.str.len = len(value_enc)

class DateField(Field):
	def _deserialize(self, pxval_value):
		return self._deserialize_days(pxval_value.lval)
	@classmethod
	def _deserialize_days(self, days):
		days_since_jan_0_0000 = c_long(days + 1721425)
		year, month, day = c_int(), c_int(), c_int()
		PX_SdnToGregorian(
			days_since_jan_0_0000, byref(year), byref(month), byref(day)
		)
		# if all values are 0, this is a blank date. return None
		if all([year.value == 0, month.value == 0, day.value == 0]):
			return None
		return date(year.value, month.value, day.value)
	def _serialize_to(self, value, pxval_value):
		pxval_value.lval = self._serialize_days(value)
	@classmethod
	def _serialize_days(cls, value):
		if value:
			sdn = PX_GregorianToSdn(value.year, value.month, value.day)
		else:
			sdn = PX_GregorianToSdn(0, 0, 0)
		return sdn - 1721425

class LongField(Field):
	def _deserialize(self, pxval_value):
		return pxval_value.lval
	def _serialize_to(self, value, pxval_value):
		pxval_value.lval = value

class DoubleField(Field):
	def _deserialize(self, pxval_value):
		return pxval_value.dval
	def _serialize_to(self, value, pxval_value):
		pxval_value.dval = value

class LogicalField(Field):
	def _deserialize(self, pxval_value):
		return bool(pxval_value.lval)
	def _serialize_to(self, value, pxval_value):
		pxval_value.lval = -1 if value else 0

class BytesField(Field):
	def _deserialize(self, pxval_value):
		return pxval_value.str.val.data[:pxval_value.str.len]
	def _serialize_to(self, value, pxval_value):
		pxval_value.str.val = value
		pxval_value.str.len = len(value)

class TimeField(Field):
	@classmethod
	def _deserialize(cls, pxval_value):
		return cls._deserialize_ms(pxval_value.lval)
	@classmethod
	def _deserialize_ms(cls, ms_since_midnight):
		ms = ms_since_midnight % 1000
		seconds_since_midnight = ms_since_midnight // 1000
		seconds = seconds_since_midnight % 60
		minutes_since_midnight = seconds_since_midnight // 60
		minutes = minutes_since_midnight % 60
		hours = minutes_since_midnight // 60
		return time(hours, minutes, seconds, ms * 1000)
	@classmethod
	def _serialize_to(cls, value, pxval_value):
		pxval_value.lval = cls._serialize_ms(value)
	@classmethod
	def _serialize_ms(cls, value):
		return value.hour * 60 * 60 * 1000 + \
			   value.minute * 60 * 1000 + \
			   value.second * 1000 + \
			   value.microsecond // 1000

class TimestampField(Field):
	@classmethod
	def _deserialize(cls, pxval_value):
		#convert dval from miliseconds to days
		days = int(pxval_value.dval / 86400000)
		ms_rem = int(pxval_value.dval % 86400000)
		date = DateField._deserialize_days(days)
		time = TimeField._deserialize_ms(ms_rem)
		return datetime.combine(date, time)
	@classmethod
	def _serialize_to(cls, value, pxval_value):
		days = DateField._serialize_days(value.date())
		ms_rem = TimeField._serialize_ms(value.time())
		pxval_value.dval = float((days * 86400000) + ms_rem)

class Row(object):
	def __init__(self, table, rownum, pxvals):
		self._table = table
		self._rownum = rownum
		self._pxvals = pxvals
	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			raise AttributeError(item)
	def __getitem__(self, item):
		field = self._table.fields[item]
		pxval = self._pxvals[field.index].contents
		return field.deserialize(pxval)
	def __setitem__(self, item, value):
		field = self._table.fields[item]
		pxval = self._pxvals[field.index].contents
		field.serialize_to(value, pxval)
	def __setattr__(self, item, value):
		if item in ('_table', '_rownum', '_pxvals'):
			super(Row, self).__setattr__(item, value)
		else:
			if item not in self._table.fields:
				raise AttributeError("can't set attribute")
			else:
				self[item] = value
	def save(self):
		result = \
			PX_update_record(self._table.pxdoc, self._pxvals, self._rownum)
		if result == -1:
			raise PXError('Could not update record.')
	def __repr__(self):
		value_strs = []
		for field_name in self._table.fields:
			try:
				value = self[field_name]
			except:
				value = '<error>'
			if value is not None:
				value_strs.append('%s=%r' % (field_name, value))
		return '%s(%s)' % (self.__class__.__name__, ', '.join(value_strs))
	def __str__(self):
		return repr(self)

class PXError(Exception):
	pass
