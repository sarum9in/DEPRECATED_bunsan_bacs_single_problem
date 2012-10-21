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

Result
^^^^^^
Result is dictionary with the following kv pairs:

   a. required fields

      1. status -> OK, WRONG_ANSWER, ... <string, enum>

   b. optional fields

      #. message -> some explanation <string>

      #. score -> the quality of result (by default is max_score if status = OK and 0 otherwise) <number>

      #. max_score -> maximum score possible (by default is 1) <number>


Example
-------

.. highlight:: python

.. doctest::

   >>> check({'in': 'path/to/1.in', 'out': 'path/to/1.out'}, {'stdin': 'path/to/input.txt', 'stdout': 'path/to/output.txt'})
   {'status': 'OK'}
   >>> check({'in': 'path/to/2.in', 'out': 'path/to/2.out'}, {'stdin': 'path/to/input.txt', 'stdout': 'path/to/output.txt'})
   {'status': 'WRONG_ANSWER', 'message': 'Even number is expected'}
   >>> check({'in': 'path/to/3.in', 'out': 'path/to/3.out'}, {'stdin': 'path/to/input.txt', 'stdout': 'path/to/output.txt'})
   {'status': 'OK', 'score': 10, 'max_score': 100}

