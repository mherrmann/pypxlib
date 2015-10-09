import ctypes
import sys

if sys.platform == 'darwin':
	# On OS X, we need to ensure that iconv is loaded before loading pxlib:
	try:
		ctypes.CDLL('/usr/lib/libiconv.dylib', ctypes.RTLD_GLOBAL)
	except OSError as e:
		raise ImportError(e)

if sys.version_info[0] == 2:
	from pxlib_generated_py2 import *
else:
	from pxlib_generated_py3 import *