import ctypes
import os.path
import sys

# Ensure that iconv is loaded before loading pxlib:
try:
	if sys.platform == 'darwin':
		ctypes.CDLL('/usr/lib/libiconv.dylib', ctypes.RTLD_GLOBAL)
	elif sys.platform == 'win32':
		ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'libiconv2.dll'))
except OSError as e:
	raise ImportError(e)

if sys.version_info[0] == 2:
	from pypxlib.pxlib_ctypes.py2 import *
else:
	from pypxlib.pxlib_ctypes.py3 import *