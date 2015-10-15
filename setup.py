"""Python bindings for the pxlib library for reading and writing Paradox
databases.

See:
https://github.com/mherrmann/pypxlib
"""

from codecs import open
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

here = abspath(dirname(__file__))

with open(join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='pypxlib',

	version='1.0',

	description='Python bindings for the pxlib library for reading and writing '
	            'Paradox databases.',
	long_description=long_description,
	url='https://github.com/mherrmann/pypxlib',

	author='Michael Herrmann',
	author_email='[my first name]@[my last name].io',

	license='GPLv2',

	platforms=['MacOS', 'Windows', 'Debian'],

	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
	
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
	
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
	
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	
		'Topic :: Database',
		'Topic :: Software Development :: Libraries'
	],

	keywords='paradox database pxlib',

	packages=['pypxlib', 'pypxlib.pxlib_ctypes'],
	package_data={
		'pypxlib.pxlib_ctypes': [
			'pxlib.dll', 'libiconv2.dll', 'libpx.dylib', 'libpx.so'
		]
	}
)