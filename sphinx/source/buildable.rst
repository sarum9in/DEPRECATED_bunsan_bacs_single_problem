Buildable
=========

Introduction
------------

For convenient standard interface for everything that may require building
such interface is introduced. Buildable specification is abstract, you may
not find directory tree here, only `Configuration file`_ format and general concepts.


Definition
----------

.. todo::

   TODO

Specifications
--------------

Configuration file
^^^^^^^^^^^^^^^^^^

Configuration file has *ini* format.
**[build]** section is used for `Buildable`_ options specifications.
User may introduce arbitrary sections except **[build]** for additional
configuration (not used by `Buildable`_).

**[build]** section contains *use* option that specifies build type.
If implementation provides default *use* value user may omit it.

Examples
````````

.. highlight:: ini

Specifies cmake builder::

   [build]
   use = cmake


Specifies single-source builder::

   [build]
   use = single
   source = main.cpp

Specifies cmake builder with non-standard config location::

   [build]
   use = cmake
   source = src/CMakeLists.txt

