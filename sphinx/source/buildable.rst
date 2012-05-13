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

**[build]** section contains *builder* option that specifies one of supported implementation supported builders.
Implementation may provide default *builder* value.

Examples
````````

.. highlight:: ini

Specifies cmake builder::

   [build]
   builder = cmake


Specifies single-source builder::

   [build]
   builder = single
   source = main.cpp

Specifies cmake builder with non-standard config location::

   [build]
   builder = cmake
   source = src/CMakeLists.txt

