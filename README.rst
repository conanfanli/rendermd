
Table of Contents
=================


* `renderme <#renderme>`_
* `Usage <#usage>`_
* `Examples <#examples>`_

  * `Inject Table of Contents <#inject-table-of-contents>`_

* `h1 <#h1>`_

  * `h2 <#h2>`_

* `h1 <#h1>`_

  * `h2 <#h2>`_
  * `Inject output of shell commands <#inject-output-of-shell-commands>`_

renderme
========

Render markdown templates.

Usage
=====

.. code-block::

   usage: rendermd [-h] [-p PATTERNS] [--no-recursive]

   Render markdown templates. This command recursively search the current
   directly and find all markdown files by matching given patterns (default to
   "**/README.md").

   optional arguments:
     -h, --help            show this help message and exit
     -p PATTERNS, --pattern PATTERNS
                           Comma separated list of markdown files to populate
     --no-recursive        Do not search for files recursively

Examples
========

Inject Table of Contents
------------------------

Before running ``rendermd``.

.. code-block:: markdown

   [//]: # (start_toc)
   [//]: # (end)

   # h1

   ## h2

After running ``rendermd``.

.. code-block:: markdown

   [//]: # (start_toc)
   Table of Contents
   =================
   - [h1](#h1)
       - [h2](#h2)

   [//]: # (end)

   # h1

   ## h2

Inject output of shell commands
-------------------------------

Before running ``rendermd``.

.. code-block:: markdown

   [//]: # (start:shell`echo success`)

success

.. code-block::


   [//]: # (end)

After running ``rendermd``.

.. code-block:: markdown

   [//]: # (start:shell`echo success`)

success

.. code-block::


   [//]: # (end)
