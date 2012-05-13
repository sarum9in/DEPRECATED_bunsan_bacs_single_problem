Validator
=========

Introduction
------------

Validator is used to check tests for correctness.

Definition
----------

Validator is function which argument is a dictionary mapping data_ids to file paths.
Validator returns boolean and possibly diagnostic message.

Example
-------

.. highlight:: python

.. doctest::

   >>> validate({'in': 'path/to/1.in', 'out': 'path/to/1.out', 'err': 'path/to/1.err'})
   (True, None)
   >>> validate({'in': 'path/to/2.in', 'out': 'path/to/2.out', 'err': 'path/to/2.err'})
   (False, 'Test is integer')


Calling conventions
-------------------

Implementation may use different wrappers to implement different calling conventions.
For instance problem author may provide executable that should be wrapped.

