"""Python bindings for the pxlib library for reading and writing Paradox
databases.

See:
https://github.com/mherrmann/pypxlib
"""

from setuptools import setup

description = \
	'Python bindings for the pxlib library for reading and writing Paradox ' \
	'databases.'
setup(
	name='pypxlib',

	version='1.9',

	description=description,
	long_description=
		description + '\n\nHome page: https://github.com/mherrmann/pypxlib',
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
			'pxlib.dll', 'pxlib_x64.dll', 'libpx.dylib', 'libpx.so'
		]
	}
)