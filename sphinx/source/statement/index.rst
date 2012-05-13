Statement
=========

Introduction
------------

Statement contains problem definition. It is essential part of the problem.
Moreover, without it problem does not exists. For different languages
and formats support `Statement version`_ entity is introduced.
Statement consists of statement versions.

Statement version
-----------------

Statement version is :doc:`../buildable`.
Each statement version is defined in configuration file.
Configuration file ends with ".ini" suffix and located in the root folder
of the statement directory.

.. highlight:: none

Consider the following directory tree::

   /en_html.ini
   /en_pdf.ini
   /en.tex
   /resources/
              schema.png
              graph.png
              file.ini

In example above we can see three ini files: "en_html.ini", "en_pdf.ini" and "file.ini".
Only "en_html.ini" and "en_pdf.ini" define statement versions.

Configuration file
------------------

Configuration file defines the following sections:

1. **[info]** defines the following options:

   a. *lang* defines statement version `Language`_

2. **[build]** section is described in particular builder specifications.

.. seealso:: `Builders list`_

Language
^^^^^^^^

Statement version is written in a particular language.
Language should be defined by the string.

Empty string is a special value treated as "unknown".
In the future empty string should not be used and all
statement version should have language specified.

Other values are specified by *BACS.WEB* project.

Builders list
-------------

Statement versions support different builders.
Default builder is :doc:`builders/copy`.

.. toctree::

   builders/index

