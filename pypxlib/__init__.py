from collections import OrderedDict
from ctypes import c_int, c_long, byref
from datetime import date
from pypxlib.pxlib_ctypes import *

import atexit
import sys

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

	def __init__(self, file_path, encoding='cp850'):
		self.file_path = file_path
		self.encoding = encoding
		self.pxdoc = PX_new()
		if PX_open_file(self.pxdoc, file_path.encode(self.PX_ENCODING)) != 0:
			raise PXError('Could not open file %s.' % self.file_path)
		self._field_indices_cached = None
	def __enter__(self):
		return self
	@property
	def fields(self):
		return list(self._field_indices)
	@property
	def _field_indices(self):
		if self._field_indices_cached is None:
			self._field_indices_cached = OrderedDict()
			num_fields = self.pxdoc.contents.px_head.contents.px_numfields
			for i in range(num_fields):
				field = PX_get_field(self.pxdoc, i).contents
				field_name = field.px_fname.data.decode(self.PX_ENCODING)
				self._field_indices_cached[field_name] = i
		return self._field_indices_cached
	def __getitem__(self, rownum):
		pxvals = PX_retrieve_record(self.pxdoc, rownum)
		if not pxvals:
			raise PXError(
				'Could not retrieve row %d of file %s.' %
				(rownum, self.file_path)
			)
		return Row(pxvals, self._field_indices, self.encoding)
	def __len__(self):
		return self.pxdoc.contents.px_head.contents.px_numrecords
	def __iter__(self):
		return Table.Iterator(self)
	def __exit__(self, *_):
		self.close()
	def close(self):
		PX_close(self.pxdoc)
		PX_delete(self.pxdoc)
		self._field_indices_cached = None

class Row(object):
	def __init__(self,  pxvals, field_indices, encoding):
		self.field_indices = field_indices
		self.pxvals = pxvals
		self.encoding = encoding
	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			return AttributeError(item)
	def __getitem__(self, item):
		pxval_index = self.field_indices[item]
		return self._parse_pxval(self.pxvals[pxval_index].contents)
	def __repr__(self):
		value_strs = []
		for field_name in self.field_indices:
			try:
				value = self[field_name]
			except:
				value = '<error>'
			if value is not None:
				value_strs.append('%s=%r' % (field_name, value))
		return '%s(%s)' % (self.__class__.__name__, ', '.join(value_strs))
	def __str__(self):
		return repr(self)
	def _parse_pxval(self, pxval):
		if pxval.isnull == b'\x01':
			return None
		type_, value = pxval.type, pxval.value
		if type_ == pxfAlpha:
			return value.str.val.data.decode(self.encoding)
		if type_ == pxfDate:
			days_since_jan_0_0000 = c_long(value.lval + 1721425)
			year, month, day = c_int(), c_int(), c_int()
			PX_SdnToGregorian(
				days_since_jan_0_0000, byref(year), byref(month), byref(day)
			)
			return datetime.date(year, month, day)
		if type_ in (pxfShort, pxfLong, pxfAutoInc):
			return value.lval
		if type_ in (pxfNumber, pxfCurrency):
			return value.dval
		if type_ == pxfLogical:
			return bool(value.lval)
		if type_ in (pxfBLOb, pxfMemoBLOb, pxfMemoBLOb, pxfBCD, pxfBytes):
			return value.str.val[:value.str.len]
		if type_ in (pxfOLE, pxfGraphic):
			return '<not supported>'
		if type_ == pxfTime:
			return self._parse_pxftime(value.lval)
		if type_ == pxfTimestamp:
			return self._parse_pxftime(int(value.dval / 86400))
		raise PXError('Unrecognized data type: %r' % type_)
	def _parse_pxftime(self, ms_since_midnight):
			ms = ms_since_midnight % 1000
			seconds_since_midnight = ms_since_midnight // 1000
			seconds = seconds_since_midnight % 60
			minutes_since_midnight = seconds_since_midnight // 60
			minutes = minutes_since_midnight % 60
			hours = minutes_since_midnight // 60
			return time(hours, minutes, seconds, ms * 1000)

class PXError(Exception):
	pass