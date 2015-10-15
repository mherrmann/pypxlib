import ctypes
import os.path
import sys

try:
	# Ensure that iconv is loaded before loading pxlib:
	if sys.platform == 'darwin':
		ctypes.CDLL('/usr/lib/libiconv.dylib', ctypes.RTLD_GLOBAL)
except OSError as e:
	raise ImportError(e)

if sys.version_info[0] == 2:
	from pypxlib.pxlib_ctypes.py2 import *
else:
	from pypxlib.pxlib_ctypes.py3 import *