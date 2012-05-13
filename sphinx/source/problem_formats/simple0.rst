"simple0" format
================

Introduction
------------

"simple0" format is the similar to bacs legacy problem format.
It uses ini files to configure problem.

Specifications
--------------

Directory tree
^^^^^^^^^^^^^^

Problem in "simple0" is a folder with the following entries:

1. *config.ini* -- `Configuration file`_

#. *checker/* -- directory with checker, see :doc:`../utilities/checker`
#. *validator/* -- directory with validator, see :doc:`../utilities/validator`
#. *statements/* -- directory with statements, see :doc:`../statements`
#. *tests/* -- directory with tests

   a. Each test is set of files which names has "test_id.data_id" format
   #. Data set of test is set of data_ids
   #. Data sets are equal among different tests
   #. Each test file is considered to be either *text* or *binary*

      i. File is considered to be *binary* if it is specified in section "[tests]" from config.ini
      #. File is considered to be *text* if it is specified in section "[tests]" from config.ini
      #. File is considered to be *text* if it is not specified


Testing algorithm
^^^^^^^^^^^^^^^^^

1. Solution testing is performed on all.
#. Test order is numeric if all test_ids match pattern ``'\d+'`` otherwise order is lexicographical.
#. Testing algorithm is *BREAK_ON_FAIL*.
#. Solution is executed on specified test.
#. After solution execution checker is executed.

Configuration file
^^^^^^^^^^^^^^^^^^

Specifications
~~~~~~~~~~~~~~

1. It has "utf8" encoding

#. It is divied into several sections

   a. **info** section has the following options

      i. name -- the name of the problem
      #. authors -- the list of authors separated by ";", author name is trimmed
      #. maintainers -- the list of maintainers separated by ";", maintainer name is trimmed
      #. source -- the source of the problem (contest name, championship...)

   #. **rlimits** section has the following options

      i. *memory* -- *uint64*, bytes **TODO units**
      #. *time* --  *uint64*, microseconds
      #. *cpu* --  *uint64*, microseconds
      #. *output* -- *uint64*, bytes

   #. **files** section has following options: *stdin*, *stdout*, *stderr*.

      i. Solution can use up to 3 files corresponding to *stdin*, *stdout* and *stderr* data streams.
      #. File ids are *stdin*, *stdout*, *stderr*.
      #. File with *stdin* id is filled from test file with ``data_id=in``.
      #. *stdout* and *stderr* may be filled by solution.
      #. If option is present no redirections are introduced for file id.
      #. If option is not present file redirection is introduced
         and file name is unspecified.

   #. **tests** section describes data set of the tests.
      You can specify file format of the data_id.

      i. ``data_id = "text"`` -- for text files
      #. ``data_id = "binary"`` -- for binary files

Examples
~~~~~~~~

Complicated sample
``````````````````
.. highlight:: ini

::

   [info]
   ; It is comment
   name="Problem name"

   ; Problem is created by "author1 <author1@example.com>" and "author2 <author2@example.com>"
   authors="author1 <author1@example.com>; author2 <author2@example.com>"

   ; Here you can specify user names/ids (related to BACS.WEB)
   ;
   ; Note that names will be trimmed, so here the following string list is specified:
   ; ["admin", "contest_admin"]
   maintainers="admin; contest_admin"

   source="PTZ summer 2011"

   [rlimits]
   ; 256MiB
   memory=268435456
   ; 1 secons
   cpu=1000000000

   [files]
   ; Note that stdin is not specified, so it is redirected from "in" file from test
   ; stdout will not be redirected
   ; stderr is redirected to file
   stdout="output.txt"

   [tests]
   ; Note that we can omit definitions of text files

   ; This line describes files such as "1.in", "2.in", "3.in" and so on
   in=text

   ; This line describes files "1.out", "2.out" ...
   out=text

   ; This line describes files "1.err", "2.err" ...
   err=text


Short sample
````````````
::

   [info]
   name="Problem name"
   maintainer="admin"

   [rlimits]
   memory=268435456
   cpu=1000000000

   [files]
   stdin="input.txt"
   stdout="output.txt"

