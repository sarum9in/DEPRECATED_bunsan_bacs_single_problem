Utilities
=========

Introduction
------------

Utilities are the entities which performs various service operations.


Buildable
---------

Each utility is :doc:`../buildable`.
If utility does not need to be build (for example it is a script)
we can treat copy operation as build.

Configuration file is named *config.ini*.


Calling conventions
-------------------

Implementation may use different wrapper to implement different calling conventions.
For instance binary executable may be wrapped for functional call.

**[utility]** section has **call** option that will be used to determine calling convention.


Builders list
-------------

Utilities support various builders (*builder* option).
Default *builder* is :doc:`builders/single`.

.. toctree::

   builders/index


Utilities list
--------------

.. toctree::

   checker
   validator

