'''Wrapper for paradox.h

Originally generated with:
ctypesgen.py -lpx /usr/local/include/paradox.h -o pxlib_generated_py2.py
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        elif isinstance(obj, bytes):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                yield os.path.abspath(name % libname)
                yield os.path.join(os.path.dirname(__file__), name % libname)
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_is_64_bit = sys.maxsize > 2 ** 32

_px_lib = 'pxlib_x64' if sys.platform == 'win32' and _is_64_bit else 'px'
_libs["px"] = load_library(_px_lib)

# 1 libraries
# End libraries

# No modules

__off_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 131

__off64_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 132

# /usr/include/libio.h: 245
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 48

_IO_lock_t = None # /usr/include/libio.h: 154

# /usr/include/libio.h: 160
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

iconv_t = POINTER(None) # /usr/include/iconv.h: 29

# /usr/local/include/paradox.h: 87
class struct_px_field(Structure):
    pass

struct_px_field.__slots__ = [
    'px_fname',
    'px_ftype',
    'px_flen',
    'px_fdc',
]
struct_px_field._fields_ = [
    ('px_fname', String),
    ('px_ftype', c_char),
    ('px_flen', c_int),
    ('px_fdc', c_int),
]

# /usr/local/include/paradox.h: 100
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'val',
    'len',
]
struct_anon_6._fields_ = [
    ('val', String),
    ('len', c_int),
]

# /usr/local/include/paradox.h: 97
class union_anon_7(Union):
    pass

union_anon_7.__slots__ = [
    'lval',
    'dval',
    'str',
]
union_anon_7._fields_ = [
    ('lval', c_long),
    ('dval', c_double),
    ('str', struct_anon_6),
]

# /usr/local/include/paradox.h: 94
class struct_px_val(Structure):
    pass

struct_px_val.__slots__ = [
    'isnull',
    'type',
    'value',
]
struct_px_val._fields_ = [
    ('isnull', c_char),
    ('type', c_int),
    ('value', union_anon_7),
]

# /usr/local/include/paradox.h: 107
class struct_px_head(Structure):
    pass

struct_px_head.__slots__ = [
    'px_tablename',
    'px_recordsize',
    'px_filetype',
    'px_fileversion',
    'px_numrecords',
    'px_theonumrecords',
    'px_numfields',
    'px_maxtablesize',
    'px_headersize',
    'px_fileblocks',
    'px_firstblock',
    'px_lastblock',
    'px_indexfieldnumber',
    'px_indexroot',
    'px_numindexlevels',
    'px_writeprotected',
    'px_doscodepage',
    'px_primarykeyfields',
    'px_modifiedflags1',
    'px_modifiedflags2',
    'px_sortorder',
    'px_autoinc',
    'px_fileupdatetime',
    'px_refintegrity',
    'px_fields',
    'px_encryption',
]
struct_px_head._fields_ = [
    ('px_tablename', String),
    ('px_recordsize', c_int),
    ('px_filetype', c_char),
    ('px_fileversion', c_int),
    ('px_numrecords', c_int),
    ('px_theonumrecords', c_int),
    ('px_numfields', c_int),
    ('px_maxtablesize', c_int),
    ('px_headersize', c_int),
    ('px_fileblocks', c_uint),
    ('px_firstblock', c_uint),
    ('px_lastblock', c_uint),
    ('px_indexfieldnumber', c_int),
    ('px_indexroot', c_int),
    ('px_numindexlevels', c_int),
    ('px_writeprotected', c_int),
    ('px_doscodepage', c_int),
    ('px_primarykeyfields', c_int),
    ('px_modifiedflags1', c_char),
    ('px_modifiedflags2', c_char),
    ('px_sortorder', c_char),
    ('px_autoinc', c_int),
    ('px_fileupdatetime', c_int),
    ('px_refintegrity', c_char),
    ('px_fields', POINTER(struct_px_field)),
    ('px_encryption', c_ulong),
]

# /usr/local/include/paradox.h: 164
class struct_px_doc(Structure):
    pass

pxdoc_t = struct_px_doc # /usr/local/include/paradox.h: 136

# /usr/local/include/paradox.h: 271
class struct_px_datablockinfo(Structure):
    pass

pxdatablockinfo_t = struct_px_datablockinfo # /usr/local/include/paradox.h: 137

# /usr/local/include/paradox.h: 245
class struct_px_blob(Structure):
    pass

pxblob_t = struct_px_blob # /usr/local/include/paradox.h: 138

pxhead_t = struct_px_head # /usr/local/include/paradox.h: 139

pxfield_t = struct_px_field # /usr/local/include/paradox.h: 140

# /usr/local/include/paradox.h: 282
class struct_px_pindex(Structure):
    pass

pxpindex_t = struct_px_pindex # /usr/local/include/paradox.h: 141

# /usr/local/include/paradox.h: 146
class struct_px_stream(Structure):
    pass

pxstream_t = struct_px_stream # /usr/local/include/paradox.h: 142

pxval_t = struct_px_val # /usr/local/include/paradox.h: 143

# /usr/local/include/paradox.h: 267
class struct_mb_head(Structure):
    pass

mbhead_t = struct_mb_head # /usr/local/include/paradox.h: 144

# /usr/local/include/paradox.h: 150
class union_anon_8(Union):
    pass

union_anon_8.__slots__ = [
    'fp',
    'stream',
]
union_anon_8._fields_ = [
    ('fp', POINTER(FILE)),
    ('stream', POINTER(None)),
]

struct_px_stream.__slots__ = [
    'type',
    'mode',
    'close',
    's',
    'read',
    'seek',
    'tell',
    'write',
]
struct_px_stream._fields_ = [
    ('type', c_int),
    ('mode', c_int),
    ('close', c_int),
    ('s', union_anon_8),
    ('read', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxdoc_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(pxdoc_t), POINTER(pxstream_t), c_long, c_int)),
    ('tell', CFUNCTYPE(UNCHECKED(c_long), POINTER(pxdoc_t), POINTER(pxstream_t))),
    ('write', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxdoc_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
]

struct_px_doc.__slots__ = [
    'px_stream',
    'px_name',
    'px_close_fp',
    'px_head',
    'px_data',
    'px_datalen',
    'px_indexdata',
    'px_indexdatalen',
    'px_pindex',
    'px_blob',
    'last_position',
    'warnings',
    'writeproc',
    'errorhandler',
    'errorhandler_user_data',
    'malloc',
    'calloc',
    'realloc',
    'free',
    'read',
    'seek',
    'tell',
    'write',
    'targetencoding',
    'inputencoding',
    'out_iconvcd',
    'in_iconvcd',
    'curblocknr',
    'curblockdirty',
    'curblock',
]
struct_px_doc._fields_ = [
    ('px_stream', POINTER(pxstream_t)),
    ('px_name', String),
    ('px_close_fp', c_int),
    ('px_head', POINTER(pxhead_t)),
    ('px_data', POINTER(None)),
    ('px_datalen', c_int),
    ('px_indexdata', POINTER(None)),
    ('px_indexdatalen', c_int),
    ('px_pindex', POINTER(pxdoc_t)),
    ('px_blob', POINTER(pxblob_t)),
    ('last_position', c_int),
    ('warnings', c_int),
    ('writeproc', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxdoc_t), POINTER(None), c_size_t)),
    ('errorhandler', CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), c_int, String, POINTER(None))),
    ('errorhandler_user_data', POINTER(None)),
    ('malloc', CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), c_size_t, String)),
    ('calloc', CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), c_size_t, String)),
    ('realloc', CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), POINTER(None), c_size_t, String)),
    ('free', CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), POINTER(None))),
    ('read', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxdoc_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(pxdoc_t), POINTER(pxstream_t), c_long, c_int)),
    ('tell', CFUNCTYPE(UNCHECKED(c_long), POINTER(pxdoc_t), POINTER(pxstream_t))),
    ('write', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxdoc_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
    ('targetencoding', String),
    ('inputencoding', String),
    ('out_iconvcd', iconv_t),
    ('in_iconvcd', iconv_t),
    ('curblocknr', c_long),
    ('curblockdirty', c_int),
    ('curblock', POINTER(c_ubyte)),
]

# /usr/local/include/paradox.h: 229
class struct_px_blockcache(Structure):
    pass

struct_px_blockcache.__slots__ = [
    'start',
    'size',
    'data',
]
struct_px_blockcache._fields_ = [
    ('start', c_long),
    ('size', c_size_t),
    ('data', POINTER(c_ubyte)),
]

pxblockcache_t = struct_px_blockcache # /usr/local/include/paradox.h: 234

# /usr/local/include/paradox.h: 236
class struct_px_mbblockinfo(Structure):
    pass

struct_px_mbblockinfo.__slots__ = [
    'number',
    'type',
    'numblobs',
    'numblocks',
    'allocspace',
]
struct_px_mbblockinfo._fields_ = [
    ('number', c_int),
    ('type', c_char),
    ('numblobs', c_char),
    ('numblocks', c_int),
    ('allocspace', c_int),
]

pxmbblockinfo_t = struct_px_mbblockinfo # /usr/local/include/paradox.h: 243

struct_px_blob.__slots__ = [
    'mb_name',
    'pxdoc',
    'mb_stream',
    'mb_head',
    'used_datablocks',
    'subblockoffset',
    'subblockinneroffset',
    'subblockfree',
    'subblockblobcount',
    'read',
    'seek',
    'tell',
    'write',
    'blockcache',
    'blocklist',
    'blocklistlen',
]
struct_px_blob._fields_ = [
    ('mb_name', String),
    ('pxdoc', POINTER(pxdoc_t)),
    ('mb_stream', POINTER(pxstream_t)),
    ('mb_head', POINTER(mbhead_t)),
    ('used_datablocks', c_int),
    ('subblockoffset', c_int),
    ('subblockinneroffset', c_int),
    ('subblockfree', c_int),
    ('subblockblobcount', c_int),
    ('read', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxblob_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(pxblob_t), POINTER(pxstream_t), c_long, c_int)),
    ('tell', CFUNCTYPE(UNCHECKED(c_long), POINTER(pxblob_t), POINTER(pxstream_t))),
    ('write', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(pxblob_t), POINTER(pxstream_t), c_size_t, POINTER(None))),
    ('blockcache', pxblockcache_t),
    ('blocklist', POINTER(pxmbblockinfo_t)),
    ('blocklistlen', c_int),
]

struct_mb_head.__slots__ = [
    'modcount',
]
struct_mb_head._fields_ = [
    ('modcount', c_int),
]

struct_px_datablockinfo.__slots__ = [
    'blockpos',
    'recordpos',
    'size',
    'recno',
    'numrecords',
    'prev',
    'next',
    'number',
]
struct_px_datablockinfo._fields_ = [
    ('blockpos', c_long),
    ('recordpos', c_long),
    ('size', c_int),
    ('recno', c_int),
    ('numrecords', c_int),
    ('prev', c_int),
    ('next', c_int),
    ('number', c_int),
]

struct_px_pindex.__slots__ = [
    'data',
    'blocknumber',
    'numrecords',
    'dummy',
    'myblocknumber',
    'level',
]
struct_px_pindex._fields_ = [
    ('data', String),
    ('blocknumber', c_int),
    ('numrecords', c_int),
    ('dummy', c_int),
    ('myblocknumber', c_int),
    ('level', c_int),
]

# /usr/local/include/paradox.h: 300
if hasattr(_libs['px'], 'PX_get_majorversion'):
    PX_get_majorversion = _libs['px'].PX_get_majorversion
    PX_get_majorversion.argtypes = []
    PX_get_majorversion.restype = c_int

# /usr/local/include/paradox.h: 303
if hasattr(_libs['px'], 'PX_get_minorversion'):
    PX_get_minorversion = _libs['px'].PX_get_minorversion
    PX_get_minorversion.argtypes = []
    PX_get_minorversion.restype = c_int

# /usr/local/include/paradox.h: 306
if hasattr(_libs['px'], 'PX_get_subminorversion'):
    PX_get_subminorversion = _libs['px'].PX_get_subminorversion
    PX_get_subminorversion.argtypes = []
    PX_get_subminorversion.restype = c_int

# /usr/local/include/paradox.h: 309
if hasattr(_libs['px'], 'PX_has_recode_support'):
    PX_has_recode_support = _libs['px'].PX_has_recode_support
    PX_has_recode_support.argtypes = []
    PX_has_recode_support.restype = c_int

# /usr/local/include/paradox.h: 312
if hasattr(_libs['px'], 'PX_has_gsf_support'):
    PX_has_gsf_support = _libs['px'].PX_has_gsf_support
    PX_has_gsf_support.argtypes = []
    PX_has_gsf_support.restype = c_int

# /usr/local/include/paradox.h: 315
if hasattr(_libs['px'], 'PX_is_bigendian'):
    PX_is_bigendian = _libs['px'].PX_is_bigendian
    PX_is_bigendian.argtypes = []
    PX_is_bigendian.restype = c_int

# /usr/local/include/paradox.h: 317
if hasattr(_libs['px'], 'PX_get_builddate'):
    PX_get_builddate = _libs['px'].PX_get_builddate
    PX_get_builddate.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        PX_get_builddate.restype = ReturnString
    else:
        PX_get_builddate.restype = String
        PX_get_builddate.errcheck = ReturnString

# /usr/local/include/paradox.h: 321
if hasattr(_libs['px'], 'PX_boot'):
    PX_boot = _libs['px'].PX_boot
    PX_boot.argtypes = []
    PX_boot.restype = None

# /usr/local/include/paradox.h: 324
if hasattr(_libs['px'], 'PX_shutdown'):
    PX_shutdown = _libs['px'].PX_shutdown
    PX_shutdown.argtypes = []
    PX_shutdown.restype = None

# /usr/local/include/paradox.h: 326
if hasattr(_libs['px'], 'PX_new3'):
    PX_new3 = _libs['px'].PX_new3
    PX_new3.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), c_int, String, POINTER(None)), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), c_size_t, String), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), POINTER(None), c_size_t, String), CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), POINTER(None)), POINTER(None)]
    PX_new3.restype = POINTER(pxdoc_t)

# /usr/local/include/paradox.h: 333
if hasattr(_libs['px'], 'PX_new2'):
    PX_new2 = _libs['px'].PX_new2
    PX_new2.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), c_int, String, POINTER(None)), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), c_size_t, String), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(pxdoc_t), POINTER(None), c_size_t, String), CFUNCTYPE(UNCHECKED(None), POINTER(pxdoc_t), POINTER(None))]
    PX_new2.restype = POINTER(pxdoc_t)

# /usr/local/include/paradox.h: 339
if hasattr(_libs['px'], 'PX_new'):
    PX_new = _libs['px'].PX_new
    PX_new.argtypes = []
    PX_new.restype = POINTER(pxdoc_t)

# /usr/local/include/paradox.h: 343
if hasattr(_libs['px'], 'PX_open_fp'):
    PX_open_fp = _libs['px'].PX_open_fp
    PX_open_fp.argtypes = [POINTER(pxdoc_t), POINTER(FILE)]
    PX_open_fp.restype = c_int

# /usr/local/include/paradox.h: 346
if hasattr(_libs['px'], 'PX_open_file'):
    PX_open_file = _libs['px'].PX_open_file
    PX_open_file.argtypes = [POINTER(pxdoc_t), String]
    PX_open_file.restype = c_int

# /usr/local/include/paradox.h: 349
if hasattr(_libs['px'], 'PX_create_file'):
    PX_create_file = _libs['px'].PX_create_file
    PX_create_file.argtypes = [POINTER(pxdoc_t), POINTER(pxfield_t), c_int, String, c_int]
    PX_create_file.restype = c_int

# /usr/local/include/paradox.h: 352
if hasattr(_libs['px'], 'PX_create_fp'):
    PX_create_fp = _libs['px'].PX_create_fp
    PX_create_fp.argtypes = [POINTER(pxdoc_t), POINTER(pxfield_t), c_int, POINTER(FILE), c_int]
    PX_create_fp.restype = c_int

# /usr/local/include/paradox.h: 354
if hasattr(_libs['px'], 'PX_get_opaque'):
    PX_get_opaque = _libs['px'].PX_get_opaque
    PX_get_opaque.argtypes = [POINTER(pxdoc_t)]
    PX_get_opaque.restype = POINTER(None)

# /usr/local/include/paradox.h: 358
if hasattr(_libs['px'], 'PX_write_primary_index'):
    PX_write_primary_index = _libs['px'].PX_write_primary_index
    PX_write_primary_index.argtypes = [POINTER(pxdoc_t), POINTER(pxdoc_t)]
    PX_write_primary_index.restype = c_int

# /usr/local/include/paradox.h: 361
if hasattr(_libs['px'], 'PX_read_primary_index'):
    PX_read_primary_index = _libs['px'].PX_read_primary_index
    PX_read_primary_index.argtypes = [POINTER(pxdoc_t)]
    PX_read_primary_index.restype = c_int

# /usr/local/include/paradox.h: 364
if hasattr(_libs['px'], 'PX_add_primary_index'):
    PX_add_primary_index = _libs['px'].PX_add_primary_index
    PX_add_primary_index.argtypes = [POINTER(pxdoc_t), POINTER(pxdoc_t)]
    PX_add_primary_index.restype = c_int

# /usr/local/include/paradox.h: 366
if hasattr(_libs['px'], 'PX_get_record'):
    PX_get_record = _libs['px'].PX_get_record
    PX_get_record.argtypes = [POINTER(pxdoc_t), c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_get_record.restype = ReturnString
    else:
        PX_get_record.restype = String
        PX_get_record.errcheck = ReturnString

# /usr/local/include/paradox.h: 369
if hasattr(_libs['px'], 'PX_get_record2'):
    PX_get_record2 = _libs['px'].PX_get_record2
    PX_get_record2.argtypes = [POINTER(pxdoc_t), c_int, String, POINTER(c_int), POINTER(pxdatablockinfo_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_get_record2.restype = ReturnString
    else:
        PX_get_record2.restype = String
        PX_get_record2.errcheck = ReturnString

# /usr/local/include/paradox.h: 373
if hasattr(_libs['px'], 'PX_put_recordn'):
    PX_put_recordn = _libs['px'].PX_put_recordn
    PX_put_recordn.argtypes = [POINTER(pxdoc_t), String, c_int]
    PX_put_recordn.restype = c_int

# /usr/local/include/paradox.h: 376
if hasattr(_libs['px'], 'PX_put_record'):
    PX_put_record = _libs['px'].PX_put_record
    PX_put_record.argtypes = [POINTER(pxdoc_t), String]
    PX_put_record.restype = c_int

# /usr/local/include/paradox.h: 379
if hasattr(_libs['px'], 'PX_insert_record'):
    PX_insert_record = _libs['px'].PX_insert_record
    PX_insert_record.argtypes = [POINTER(pxdoc_t), POINTER(POINTER(pxval_t))]
    PX_insert_record.restype = c_int

# /usr/local/include/paradox.h: 382
if hasattr(_libs['px'], 'PX_update_record'):
    PX_update_record = _libs['px'].PX_update_record
    PX_update_record.argtypes = [POINTER(pxdoc_t), POINTER(POINTER(pxval_t)), c_int]
    PX_update_record.restype = c_int

# /usr/local/include/paradox.h: 385
if hasattr(_libs['px'], 'PX_delete_record'):
    PX_delete_record = _libs['px'].PX_delete_record
    PX_delete_record.argtypes = [POINTER(pxdoc_t), c_int]
    PX_delete_record.restype = c_int

# /usr/local/include/paradox.h: 387
if hasattr(_libs['px'], 'PX_retrieve_record'):
    PX_retrieve_record = _libs['px'].PX_retrieve_record
    PX_retrieve_record.argtypes = [POINTER(pxdoc_t), c_int]
    PX_retrieve_record.restype = POINTER(POINTER(pxval_t))

# /usr/local/include/paradox.h: 391
if hasattr(_libs['px'], 'PX_close'):
    PX_close = _libs['px'].PX_close
    PX_close.argtypes = [POINTER(pxdoc_t)]
    PX_close.restype = None

# /usr/local/include/paradox.h: 394
if hasattr(_libs['px'], 'PX_delete'):
    PX_delete = _libs['px'].PX_delete
    PX_delete.argtypes = [POINTER(pxdoc_t)]
    PX_delete.restype = None

# /usr/local/include/paradox.h: 397
if hasattr(_libs['px'], 'PX_pack'):
    PX_pack = _libs['px'].PX_pack
    PX_pack.argtypes = [POINTER(pxdoc_t)]
    PX_pack.restype = c_int

# /usr/local/include/paradox.h: 399
if hasattr(_libs['px'], 'PX_get_fields'):
    PX_get_fields = _libs['px'].PX_get_fields
    PX_get_fields.argtypes = [POINTER(pxdoc_t)]
    PX_get_fields.restype = POINTER(pxfield_t)

# /usr/local/include/paradox.h: 402
if hasattr(_libs['px'], 'PX_get_field'):
    PX_get_field = _libs['px'].PX_get_field
    PX_get_field.argtypes = [POINTER(pxdoc_t), c_int]
    PX_get_field.restype = POINTER(pxfield_t)

# /usr/local/include/paradox.h: 406
if hasattr(_libs['px'], 'PX_get_num_fields'):
    PX_get_num_fields = _libs['px'].PX_get_num_fields
    PX_get_num_fields.argtypes = [POINTER(pxdoc_t)]
    PX_get_num_fields.restype = c_int

# /usr/local/include/paradox.h: 409
if hasattr(_libs['px'], 'PX_get_num_records'):
    PX_get_num_records = _libs['px'].PX_get_num_records
    PX_get_num_records.argtypes = [POINTER(pxdoc_t)]
    PX_get_num_records.restype = c_int

# /usr/local/include/paradox.h: 412
if hasattr(_libs['px'], 'PX_get_recordsize'):
    PX_get_recordsize = _libs['px'].PX_get_recordsize
    PX_get_recordsize.argtypes = [POINTER(pxdoc_t)]
    PX_get_recordsize.restype = c_int

# /usr/local/include/paradox.h: 415
if hasattr(_libs['px'], 'PX_set_parameter'):
    PX_set_parameter = _libs['px'].PX_set_parameter
    PX_set_parameter.argtypes = [POINTER(pxdoc_t), String, String]
    PX_set_parameter.restype = c_int

# /usr/local/include/paradox.h: 418
if hasattr(_libs['px'], 'PX_get_parameter'):
    PX_get_parameter = _libs['px'].PX_get_parameter
    PX_get_parameter.argtypes = [POINTER(pxdoc_t), String, POINTER(POINTER(c_char))]
    PX_get_parameter.restype = c_int

# /usr/local/include/paradox.h: 421
if hasattr(_libs['px'], 'PX_set_value'):
    PX_set_value = _libs['px'].PX_set_value
    PX_set_value.argtypes = [POINTER(pxdoc_t), String, c_float]
    PX_set_value.restype = c_int

# /usr/local/include/paradox.h: 424
if hasattr(_libs['px'], 'PX_get_value'):
    PX_get_value = _libs['px'].PX_get_value
    PX_get_value.argtypes = [POINTER(pxdoc_t), String, POINTER(c_float)]
    PX_get_value.restype = c_int

# /usr/local/include/paradox.h: 427
if hasattr(_libs['px'], 'PX_set_targetencoding'):
    PX_set_targetencoding = _libs['px'].PX_set_targetencoding
    PX_set_targetencoding.argtypes = [POINTER(pxdoc_t), String]
    PX_set_targetencoding.restype = c_int

# /usr/local/include/paradox.h: 430
if hasattr(_libs['px'], 'PX_set_inputencoding'):
    PX_set_inputencoding = _libs['px'].PX_set_inputencoding
    PX_set_inputencoding.argtypes = [POINTER(pxdoc_t), String]
    PX_set_inputencoding.restype = c_int

# /usr/local/include/paradox.h: 433
if hasattr(_libs['px'], 'PX_set_tablename'):
    PX_set_tablename = _libs['px'].PX_set_tablename
    PX_set_tablename.argtypes = [POINTER(pxdoc_t), String]
    PX_set_tablename.restype = c_int

# /usr/local/include/paradox.h: 436
if hasattr(_libs['px'], 'PX_set_blob_file'):
    PX_set_blob_file = _libs['px'].PX_set_blob_file
    PX_set_blob_file.argtypes = [POINTER(pxdoc_t), String]
    PX_set_blob_file.restype = c_int

# /usr/local/include/paradox.h: 439
if hasattr(_libs['px'], 'PX_set_blob_fp'):
    PX_set_blob_fp = _libs['px'].PX_set_blob_fp
    PX_set_blob_fp.argtypes = [POINTER(pxdoc_t), POINTER(FILE)]
    PX_set_blob_fp.restype = c_int

# /usr/local/include/paradox.h: 442
if hasattr(_libs['px'], 'PX_has_blob_file'):
    PX_has_blob_file = _libs['px'].PX_has_blob_file
    PX_has_blob_file.argtypes = [POINTER(pxdoc_t)]
    PX_has_blob_file.restype = c_int

# /usr/local/include/paradox.h: 444
if hasattr(_libs['px'], 'PX_new_blob'):
    PX_new_blob = _libs['px'].PX_new_blob
    PX_new_blob.argtypes = [POINTER(pxdoc_t)]
    PX_new_blob.restype = POINTER(pxblob_t)

# /usr/local/include/paradox.h: 448
if hasattr(_libs['px'], 'PX_open_blob_fp'):
    PX_open_blob_fp = _libs['px'].PX_open_blob_fp
    PX_open_blob_fp.argtypes = [POINTER(pxblob_t), POINTER(FILE)]
    PX_open_blob_fp.restype = c_int

# /usr/local/include/paradox.h: 451
if hasattr(_libs['px'], 'PX_open_blob_file'):
    PX_open_blob_file = _libs['px'].PX_open_blob_file
    PX_open_blob_file.argtypes = [POINTER(pxblob_t), String]
    PX_open_blob_file.restype = c_int

# /usr/local/include/paradox.h: 454
if hasattr(_libs['px'], 'PX_create_blob_fp'):
    PX_create_blob_fp = _libs['px'].PX_create_blob_fp
    PX_create_blob_fp.argtypes = [POINTER(pxblob_t), POINTER(FILE)]
    PX_create_blob_fp.restype = c_int

# /usr/local/include/paradox.h: 457
if hasattr(_libs['px'], 'PX_create_blob_file'):
    PX_create_blob_file = _libs['px'].PX_create_blob_file
    PX_create_blob_file.argtypes = [POINTER(pxblob_t), String]
    PX_create_blob_file.restype = c_int

# /usr/local/include/paradox.h: 460
if hasattr(_libs['px'], 'PX_close_blob'):
    PX_close_blob = _libs['px'].PX_close_blob
    PX_close_blob.argtypes = [POINTER(pxblob_t)]
    PX_close_blob.restype = None

# /usr/local/include/paradox.h: 463
if hasattr(_libs['px'], 'PX_delete_blob'):
    PX_delete_blob = _libs['px'].PX_delete_blob
    PX_delete_blob.argtypes = [POINTER(pxblob_t)]
    PX_delete_blob.restype = None

# /usr/local/include/paradox.h: 465
if hasattr(_libs['px'], 'PX_read_blobdata'):
    PX_read_blobdata = _libs['px'].PX_read_blobdata
    PX_read_blobdata.argtypes = [POINTER(pxblob_t), String, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_read_blobdata.restype = ReturnString
    else:
        PX_read_blobdata.restype = String
        PX_read_blobdata.errcheck = ReturnString

# /usr/local/include/paradox.h: 468
if hasattr(_libs['px'], 'PX_read_graphicdata'):
    PX_read_graphicdata = _libs['px'].PX_read_graphicdata
    PX_read_graphicdata.argtypes = [POINTER(pxblob_t), String, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_read_graphicdata.restype = ReturnString
    else:
        PX_read_graphicdata.restype = String
        PX_read_graphicdata.errcheck = ReturnString

# /usr/local/include/paradox.h: 471
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'PX_read_grahicdata'):
        continue
    PX_read_grahicdata = _lib.PX_read_grahicdata
    PX_read_grahicdata.argtypes = [POINTER(pxblob_t), String, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_read_grahicdata.restype = ReturnString
    else:
        PX_read_grahicdata.restype = String
        PX_read_grahicdata.errcheck = ReturnString
    break

# /usr/local/include/paradox.h: 477
if hasattr(_libs['px'], 'PX_get_data_alpha'):
    PX_get_data_alpha = _libs['px'].PX_get_data_alpha
    PX_get_data_alpha.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(POINTER(c_char))]
    PX_get_data_alpha.restype = c_int

# /usr/local/include/paradox.h: 480
if hasattr(_libs['px'], 'PX_get_data_bytes'):
    PX_get_data_bytes = _libs['px'].PX_get_data_bytes
    PX_get_data_bytes.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(POINTER(c_char))]
    PX_get_data_bytes.restype = c_int

# /usr/local/include/paradox.h: 483
if hasattr(_libs['px'], 'PX_get_data_double'):
    PX_get_data_double = _libs['px'].PX_get_data_double
    PX_get_data_double.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(c_double)]
    PX_get_data_double.restype = c_int

# /usr/local/include/paradox.h: 486
if hasattr(_libs['px'], 'PX_get_data_long'):
    PX_get_data_long = _libs['px'].PX_get_data_long
    PX_get_data_long.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(c_long)]
    PX_get_data_long.restype = c_int

# /usr/local/include/paradox.h: 489
if hasattr(_libs['px'], 'PX_get_data_short'):
    PX_get_data_short = _libs['px'].PX_get_data_short
    PX_get_data_short.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(c_int)]
    PX_get_data_short.restype = c_int

# /usr/local/include/paradox.h: 492
if hasattr(_libs['px'], 'PX_get_data_byte'):
    PX_get_data_byte = _libs['px'].PX_get_data_byte
    PX_get_data_byte.argtypes = [POINTER(pxdoc_t), String, c_int, String]
    PX_get_data_byte.restype = c_int

# /usr/local/include/paradox.h: 495
if hasattr(_libs['px'], 'PX_get_data_bcd'):
    PX_get_data_bcd = _libs['px'].PX_get_data_bcd
    PX_get_data_bcd.argtypes = [POINTER(pxdoc_t), POINTER(c_ubyte), c_int, POINTER(POINTER(c_char))]
    PX_get_data_bcd.restype = c_int

# /usr/local/include/paradox.h: 498
if hasattr(_libs['px'], 'PX_get_data_blob'):
    PX_get_data_blob = _libs['px'].PX_get_data_blob
    PX_get_data_blob.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_char))]
    PX_get_data_blob.restype = c_int

# /usr/local/include/paradox.h: 501
if hasattr(_libs['px'], 'PX_get_data_graphic'):
    PX_get_data_graphic = _libs['px'].PX_get_data_graphic
    PX_get_data_graphic.argtypes = [POINTER(pxdoc_t), String, c_int, POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_char))]
    PX_get_data_graphic.restype = c_int

# /usr/local/include/paradox.h: 505
if hasattr(_libs['px'], 'PX_put_data_alpha'):
    PX_put_data_alpha = _libs['px'].PX_put_data_alpha
    PX_put_data_alpha.argtypes = [POINTER(pxdoc_t), String, c_int, String]
    PX_put_data_alpha.restype = None

# /usr/local/include/paradox.h: 508
if hasattr(_libs['px'], 'PX_put_data_bytes'):
    PX_put_data_bytes = _libs['px'].PX_put_data_bytes
    PX_put_data_bytes.argtypes = [POINTER(pxdoc_t), String, c_int, String]
    PX_put_data_bytes.restype = None

# /usr/local/include/paradox.h: 511
if hasattr(_libs['px'], 'PX_put_data_double'):
    PX_put_data_double = _libs['px'].PX_put_data_double
    PX_put_data_double.argtypes = [POINTER(pxdoc_t), String, c_int, c_double]
    PX_put_data_double.restype = None

# /usr/local/include/paradox.h: 514
if hasattr(_libs['px'], 'PX_put_data_long'):
    PX_put_data_long = _libs['px'].PX_put_data_long
    PX_put_data_long.argtypes = [POINTER(pxdoc_t), String, c_int, c_int]
    PX_put_data_long.restype = None

# /usr/local/include/paradox.h: 517
if hasattr(_libs['px'], 'PX_put_data_short'):
    PX_put_data_short = _libs['px'].PX_put_data_short
    PX_put_data_short.argtypes = [POINTER(pxdoc_t), String, c_int, c_int]
    PX_put_data_short.restype = None

# /usr/local/include/paradox.h: 520
if hasattr(_libs['px'], 'PX_put_data_byte'):
    PX_put_data_byte = _libs['px'].PX_put_data_byte
    PX_put_data_byte.argtypes = [POINTER(pxdoc_t), String, c_int, c_char]
    PX_put_data_byte.restype = None

# /usr/local/include/paradox.h: 523
if hasattr(_libs['px'], 'PX_put_data_bcd'):
    PX_put_data_bcd = _libs['px'].PX_put_data_bcd
    PX_put_data_bcd.argtypes = [POINTER(pxdoc_t), String, c_int, String]
    PX_put_data_bcd.restype = None

# /usr/local/include/paradox.h: 526
if hasattr(_libs['px'], 'PX_put_data_blob'):
    PX_put_data_blob = _libs['px'].PX_put_data_blob
    PX_put_data_blob.argtypes = [POINTER(pxdoc_t), String, c_int, String, c_int]
    PX_put_data_blob.restype = c_int

# /usr/local/include/paradox.h: 529
if hasattr(_libs['px'], 'PX_SdnToGregorian'):
    PX_SdnToGregorian = _libs['px'].PX_SdnToGregorian
    PX_SdnToGregorian.argtypes = [c_long, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    PX_SdnToGregorian.restype = None

# /usr/local/include/paradox.h: 532
if hasattr(_libs['px'], 'PX_GregorianToSdn'):
    PX_GregorianToSdn = _libs['px'].PX_GregorianToSdn
    PX_GregorianToSdn.argtypes = [c_int, c_int, c_int]
    PX_GregorianToSdn.restype = c_long

# /usr/local/include/paradox.h: 534
if hasattr(_libs['px'], 'PX_make_time'):
    PX_make_time = _libs['px'].PX_make_time
    PX_make_time.argtypes = [POINTER(pxdoc_t), c_int, c_int, c_int]
    PX_make_time.restype = POINTER(pxval_t)

# /usr/local/include/paradox.h: 537
if hasattr(_libs['px'], 'PX_make_date'):
    PX_make_date = _libs['px'].PX_make_date
    PX_make_date.argtypes = [POINTER(pxdoc_t), c_int, c_int, c_int]
    PX_make_date.restype = POINTER(pxval_t)

# /usr/local/include/paradox.h: 540
if hasattr(_libs['px'], 'PX_make_timestamp'):
    PX_make_timestamp = _libs['px'].PX_make_timestamp
    PX_make_timestamp.argtypes = [POINTER(pxdoc_t), c_int, c_int, c_int, c_int, c_int, c_int]
    PX_make_timestamp.restype = POINTER(pxval_t)

# /usr/local/include/paradox.h: 543
if hasattr(_libs['px'], 'PX_timestamp2string'):
    PX_timestamp2string = _libs['px'].PX_timestamp2string
    PX_timestamp2string.argtypes = [POINTER(pxdoc_t), c_double, String]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_timestamp2string.restype = ReturnString
    else:
        PX_timestamp2string.restype = String
        PX_timestamp2string.errcheck = ReturnString

# /usr/local/include/paradox.h: 546
if hasattr(_libs['px'], 'PX_time2string'):
    PX_time2string = _libs['px'].PX_time2string
    PX_time2string.argtypes = [POINTER(pxdoc_t), c_long, String]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_time2string.restype = ReturnString
    else:
        PX_time2string.restype = String
        PX_time2string.errcheck = ReturnString

# /usr/local/include/paradox.h: 549
if hasattr(_libs['px'], 'PX_date2string'):
    PX_date2string = _libs['px'].PX_date2string
    PX_date2string.argtypes = [POINTER(pxdoc_t), c_long, String]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_date2string.restype = ReturnString
    else:
        PX_date2string.restype = String
        PX_date2string.errcheck = ReturnString

# /usr/local/include/paradox.h: 552
if hasattr(_libs['px'], 'PX_strdup'):
    PX_strdup = _libs['px'].PX_strdup
    PX_strdup.argtypes = [POINTER(pxdoc_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        PX_strdup.restype = ReturnString
    else:
        PX_strdup.restype = String
        PX_strdup.errcheck = ReturnString

# /usr/local/include/paradox.h: 4
try:
    PX_USE_RECODE = 0
except:
    pass

# /usr/local/include/paradox.h: 5
try:
    PX_USE_ICONV = 1
except:
    pass

# /usr/local/include/paradox.h: 38
try:
    px_true = 1
except:
    pass

# /usr/local/include/paradox.h: 39
try:
    px_false = 0
except:
    pass

# /usr/local/include/paradox.h: 42
try:
    PX_MemoryError = 1
except:
    pass

# /usr/local/include/paradox.h: 43
try:
    PX_IOError = 2
except:
    pass

# /usr/local/include/paradox.h: 44
try:
    PX_RuntimeError = 3
except:
    pass

# /usr/local/include/paradox.h: 45
try:
    PX_Warning = 100
except:
    pass

# /usr/local/include/paradox.h: 48
try:
    pxfIOFile = 1
except:
    pass

# /usr/local/include/paradox.h: 50
try:
    pxfIOStream = 3
except:
    pass

# /usr/local/include/paradox.h: 53
try:
    pxfAlpha = 1
except:
    pass

# /usr/local/include/paradox.h: 54
try:
    pxfDate = 2
except:
    pass

# /usr/local/include/paradox.h: 55
try:
    pxfShort = 3
except:
    pass

# /usr/local/include/paradox.h: 56
try:
    pxfLong = 4
except:
    pass

# /usr/local/include/paradox.h: 57
try:
    pxfCurrency = 5
except:
    pass

# /usr/local/include/paradox.h: 58
try:
    pxfNumber = 6
except:
    pass

# /usr/local/include/paradox.h: 59
try:
    pxfLogical = 9
except:
    pass

# /usr/local/include/paradox.h: 60
try:
    pxfMemoBLOb = 12
except:
    pass

# /usr/local/include/paradox.h: 61
try:
    pxfBLOb = 13
except:
    pass

# /usr/local/include/paradox.h: 62
try:
    pxfFmtMemoBLOb = 14
except:
    pass

# /usr/local/include/paradox.h: 63
try:
    pxfOLE = 15
except:
    pass

# /usr/local/include/paradox.h: 64
try:
    pxfGraphic = 16
except:
    pass

# /usr/local/include/paradox.h: 65
try:
    pxfTime = 20
except:
    pass

# /usr/local/include/paradox.h: 66
try:
    pxfTimestamp = 21
except:
    pass

# /usr/local/include/paradox.h: 67
try:
    pxfAutoInc = 22
except:
    pass

# /usr/local/include/paradox.h: 68
try:
    pxfBCD = 23
except:
    pass

# /usr/local/include/paradox.h: 69
try:
    pxfBytes = 24
except:
    pass

# /usr/local/include/paradox.h: 70
try:
    pxfNumTypes = 24
except:
    pass

# /usr/local/include/paradox.h: 73
try:
    pxfFileTypIndexDB = 0
except:
    pass

# /usr/local/include/paradox.h: 74
try:
    pxfFileTypPrimIndex = 1
except:
    pass

# /usr/local/include/paradox.h: 75
try:
    pxfFileTypNonIndexDB = 2
except:
    pass

# /usr/local/include/paradox.h: 76
try:
    pxfFileTypNonIncSecIndex = 3
except:
    pass

# /usr/local/include/paradox.h: 77
try:
    pxfFileTypSecIndex = 4
except:
    pass

# /usr/local/include/paradox.h: 78
try:
    pxfFileTypIncSecIndex = 5
except:
    pass

# /usr/local/include/paradox.h: 79
try:
    pxfFileTypNonIncSecIndexG = 6
except:
    pass

# /usr/local/include/paradox.h: 80
try:
    pxfFileTypSecIndexG = 7
except:
    pass

# /usr/local/include/paradox.h: 81
try:
    pxfFileTypIncSecIndexG = 8
except:
    pass

# /usr/local/include/paradox.h: 84
try:
    pxfFileRead = 1
except:
    pass

# /usr/local/include/paradox.h: 85
try:
    pxfFileWrite = 2
except:
    pass

px_field = struct_px_field # /usr/local/include/paradox.h: 87

px_val = struct_px_val # /usr/local/include/paradox.h: 94

px_head = struct_px_head # /usr/local/include/paradox.h: 107

px_doc = struct_px_doc # /usr/local/include/paradox.h: 164

px_datablockinfo = struct_px_datablockinfo # /usr/local/include/paradox.h: 271

px_blob = struct_px_blob # /usr/local/include/paradox.h: 245

px_pindex = struct_px_pindex # /usr/local/include/paradox.h: 282

px_stream = struct_px_stream # /usr/local/include/paradox.h: 146

mb_head = struct_mb_head # /usr/local/include/paradox.h: 267

px_blockcache = struct_px_blockcache # /usr/local/include/paradox.h: 229

px_mbblockinfo = struct_px_mbblockinfo # /usr/local/include/paradox.h: 236

# No inserted files

