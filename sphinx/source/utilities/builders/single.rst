"single" builder
================

Introduction
------------

"single" builder provides simple way to compile
*single-source* utility. It is created for simplest cases,
so it lacks a lot of functionality. If you need complex build
you should not use this builder. But for something simple
it is preferable.

*Single-source* utility is compilable with single command.


Specifications
--------------

Configuration file
^^^^^^^^^^^^^^^^^^

**[build]** section of configuration file
contains the following options:

1. *source* specifies source file
#. *std* specifies programming language standard, default is the newest language standard.
   For some languages compiler name may used.
#. *libs* specifies library list "\\n" separated
#. *call* specifies calling convention **TODO move up/describe/default value**


Programming languages
^^^^^^^^^^^^^^^^^^^^^

**TODO**

Examples
--------

.. highlight:: ini

::

   [build]
   builder = single
   source = main.cpp

Example with specified standard::

   [build]
   builder = single
   source = main.pas
   std = fpc

Example with testlib::

   [build]
   builder = single
   source = main.dpr
   libs = some_testlib

