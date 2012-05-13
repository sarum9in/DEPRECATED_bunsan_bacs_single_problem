Checker
=======

Introduction
------------

Checker is used to validate solution output.


Definition
----------

Checker is a function which arguments are to dictionaries.
First dictionary maps data_ids to test file paths.
Second dictionary maps solution file ids to file paths.
Result is enumerator with probably diagnostic message.


Example
-------

.. highlight:: python

.. doctest::

   >>> check({'in': 'path/to/1.in', 'out': 'path/to/1.out'}, {'stdin': 'path/to/input.txt', 'stdout': 'path/to/output.txt'})
   ('OK', None)
   >>> check({'in': 'path/to/2.in', 'out': 'path/to/2.out'}, {'stdin': 'path/to/input.txt', 'stdout': 'path/to/output.txt'})
   ('WRONG_ANSWER', 'Even number is expected')


Calling conventions
-------------------

Implementation may use different wrapper to implement
different calling conventions.
For instance binary checker may be wrapped for functional call.

