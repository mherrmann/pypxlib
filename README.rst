pypxlib
=======

Python bindings for the `pxlib library`_ for reading and writing Paradox
databases. The version of pxlib currently exposed by pypxlib is 0.6.5.

.. _`pxlib library`: http://pxlib.sourceforge.net/

Usage
=====

pypxlib exposes a high-level API for reading Paradox databases. To use
this API, you need the following import:

.. code:: python

    from pypxlib import Table

Get the field names in a table:

.. code:: python

    >>> table = Table('data.db')
    >>> table.fields
    ['field1', 'field2', 'field3']

Get the number of rows:

.. code:: python

    >>> len(table)
    123

Get the first row:

.. code:: python

    >>> row = table[0]
    >>> row
    Row(field1='foo', field2=13, field3=True)

Access a row’s properties:

.. code:: python

    >>> row.field1
    'foo'
    >>> row['field1']
    'foo'

Iterate over all rows:

.. code:: python

    >>> for row in table:
    ...    print(row)
    ...
    Row(field1='foo', field2=13, field3=True)
    Row(field2='bar', field2=87, field3=True)
    ...

Don’t forget to close the table!

.. code:: python

    table = Table('data.db')
    try:
        # Process the table...
    finally:
        table.close()

Or use it as a context manager:

.. code:: python

    with Table('data.db') as table:
        # Process the table...

Access to pxlib via ctypes
--------------------------

pypxlib is esentially a thin wrapper around the pxlib C library. The
high-level API described above makes it easy to *read* tables. If you
also need to write to a table, or another more complicated use case,
then you can fall back to the ctypes bindings of pxlib exposed by this
library:

.. code:: python

    from pypxlib.pxlib_ctypes import *

    pxdoc = PX_new()
    PX_open_file(pxdoc, b"test.db")

    num_fields = PX_get_num_fields(pxdoc)
    print('test.db has %d fields:' % num_fields)

    for i in range(num_fields):
        field = PX_get_field(pxdoc, i)
        print(field.contents.px_fname)

    # Close the file:
    PX_close(pxdoc)
    # Free the memory associated with pxdoc:
    PX_delete(pxdoc)

All the ``PX_...`` functions come directly from the `list of pxlibs functions`_.
Note that you do not need to call ``PX_boot()`` and ``PX_shutdown``, as these
functions are already called when importing ``pypxlib``, and via an
``atexit`` handler.

.. _`list of pxlibs functions`: http://pxlib.sourceforge.net/documentation.php

Dynamic libraries in this repository
====================================

Here is a list of dynamic libraries contained in this repository, and
how they were obtained:

* ``libpx.so``, ``pxlib.dll``, ``libpx.dylib`` were obtained from building
  pxlib 0.6.5 on Ubuntu 14.0.4.1, Windows 7 and Mac OS X 10.10.5, respectively.
  See *Building pxlib* below.
* ``libiconv2.dll`` was downloaded as part of the *Binaries* zip file from
  ``http://gnuwin32.sourceforge.net/packages/libiconv.htm``. Its version is
  1.9.2-1.

Building pxlib
==============

This project contains dynamic libraries for version 0.6.5 of the pxlib
library. Here, the steps that were necessary to compile the library on
the various operating systems are documented.

Ubuntu 14.04.1 LTS
------------------

.. code:: bash

    sudo apt-get update
    sudo apt-get install build-essential
    wget 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.5/pxlib-0.6.5.tar.gz?ts='`date +%s`'&use_mirror=freefr' -o pxlib-0.6.5.tar.gz
    tar -zxvf pxlib-0.6.5.tar.gz
    cd pxlib-0.6.5/
    ./configure
    make
    sudo make install

OS X 10.10.5
------------

.. code:: bash

    sudo brew install intltool
    sudo brew link xy
    sudo brew install gettext
    curl -L 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.5/pxlib-0.6.5.tar.gz?ts='`date +%s`'&use_mirror=freefr' -o pxlib-0.6.5.tar.gz
    tar -zxvf pxlib-0.6.5.tar.gz
    cd pxlib-0.6.5/
    echo './configure --prefix=out' | brew sh
    sed -i '' 's/#define HAVE_LOCALE_H 1//' config.h
    make
    make install

Windows 7
---------

1.  Download and install Visual Studio Community 2015.
2.  Download and install CMake.
3.  Download the pxlib 0.6.5 sources from
    ``http://sourceforge.net/projects/pxlib/files/latest/download?source=files``.
4.  Extract the pxlib sources to a directory, eg. ``C:\pxlib-0.6.5``.
5.  Download libiconv-1.9.2-1-lib.zip from
    ``http://sourceforge.net/projects/gnuwin32/files/libiconv/1.9.2-1/libiconv-1.9.2-1-lib.zip/download``.
6.  Extract libiconv-1.9.2-1-lib.zip into ``C:\pxlib-0.6.5``.
7.  Open ``C:\pxlib-0.6.5\CMakeLists.txt`` with a text editor and add
    the following line before ``check_include_file("iconv.h" ...)``:
    ``set(CMAKE_REQUIRED_INCLUDES ${CMAKE_SOURCE_DIR}/include)``.
8.  Also add the line
    ``TARGET_LINK_LIBRARIES(pxlib ${CMAKE_SOURCE_DIR}/lib/libiconv.lib)``
    to the end of the file.
9.  Open a command prompt and cd to ``C:\pxlib-0.6.5``.
10. Run ``cmake .``.
11. Open the generated file ``C:\pxlib-0.6.5\ALL_BUILD.vcxproj`` in
    Visual Studio.
12. Under ``Build`` select ``Configuration Manager``. Select
    Configuration ``Release`` for Project ``pxlib``.
13. Click ``Build/Build Solution``.