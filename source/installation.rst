############
Installation
############

.. admonition:: Keep the following in mind

    - AstroConda supports Linux (>=glibc-2.12) and OS X (>= 10.7; 10.6 is NOT supported); Running Python 2.7, 3.4, or 3.5.
    - If IRAF is required as part of your personal workflow it is *highly recommended* you install Anaconda2 (`FAQ <faq.html#why-is-iraf-pyraf-less-functional-under-python-3>`_).
    - Otherwise choose the Anaconda installer best suited for your scripting needs.
    - This documentation specifically targets Anaconda3 installations. However, the same commands should still work interchangeably between versions.

Obtain Anaconda
===============

Go grab a copy of the `Anaconda <https://www.continuum.io/downloads>`_ distribution from Continuum Analytics, Inc. Be sure to select
the installation medium appropriate for your operating system and architecture.

Installation instructions for your platform are also available on the download page.

.. tip::

    Are you using ``bash`` as your shell? Run ``echo $SHELL`` in a terminal and make sure it says something like ``/bin/bash``.
    If it does not, you will have to change your default shell (which is outside the scope of these instructions).
    In the meantime, you can start ``bash -l`` from within your terminal to use ``bash`` temporarily to follow these instructions.


Configure Conda
===============

In order to install packages directly from the AstroConda repository, you will need to configure Anaconda to do so.
This will permanently add the repository to Conda's search path. Be aware that adding additional
`anaconda.org <https://anaconda.org>`_ or direct-url repositories may affect the stability of AstroConda's run-time
environment.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc


Install AstroConda
==================

Now that Conda is configured to pull from our repository, you may now go ahead and install the ``stsci`` metapackage.
The example below will generate a new environment called "astroconda" (using the ``-n`` flag),
however, this is merely a suggestion. Feel free to use a name that works best for you.

.. code-block:: sh

    $ conda create -n astroconda stsci
    $ source activate astroconda


Fine-tuning the installation
============================

If you are short on hard drive space, have a slow internet connection, or are simply not interested in installing
*everything but the kitchen sink*; please feel free to peruse the `manifest <http://ssb.stsci.edu/astroconda>`_ and
install a custom mix of packages *tailored to your needs*.

.. code-block:: sh

    $ conda create -n astroconda [package [package ...]]
    $ source activate astroconda



