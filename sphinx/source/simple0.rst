"simple0" format
================

Introduction
------------

"simple0" format is the similar to bacs legacy problem format.
It uses ini files to configure problem.

Directory tree
**************

Problem in "simple0" is a folder with the following entries:

1. *config.ini* -- configuration file

   a. It has "utf8" encoding

   #. It is divied into several sections

      i. **info** section has the following options

         a. name -- the name of the problem
         #. authors -- the list of authors separated by ";", author name is trimmed
         #. maintainers -- the list of maintainers separated by ";", maintainer name is trimmed
         #. source -- the source of the problem (contest name, championship...)

      #. **rlimits** section has the following options

         a. memory
         #. time
         #. cpu
         #. output

      #. **files** section has the following options

         a. stdin
         #. stdout
         #. stderr

      #. **tests** section

         a. **TODO**

#. *checker/* -- directory with checker, see :doc:`buildable`
#. *validator/* -- directory with validator, see :doc:`buildable`
#. *statements/* -- directory with statements, see :doc:`buildable`

   a. **TODO**

#. *tests/* -- directory with tests

   a. Each test is set of files which names has "test_id.data_id" format
   #. Data set of test is set of data_ids
   #. Data sets are equal among different tests
   #. Each test file is considered to be either *text* or *binary*

      i. File is considered to be *binary* if it is specified in section "[tests]" from config.ini
      #. File is considered to be *text* if it is specified in section "[tests]" from config.ini
      #. File is considered to be *text* if it is not specified

