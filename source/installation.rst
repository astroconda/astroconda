############
Installation
############

Before you begin, the list below contains known requirements and limitations of AstroConda:

    - This documentation targets Anaconda3 (i.e. Python 3), but the installation instructions work equally well with any of the Anaconda distributions.
    - AstroConda supports Linux (glibc ≥ 2.12) and Mac OS X (≥ 10.7; 10.6 is NOT supported)
    - AstroConda contains packages for 64-bit [#archnote]_ Python 2.7 and 3.5.
    - Conda only supports BASH and ZSH environments. If you are a native CSH user, execute ``bash -l`` prior to performing the procedures detailed in this guide.
    - IRAF users: After configuring Anaconda for use with AstroConda, refer to the :ref:`iraf_install` section of this guide to continue your installation.

Obtain Anaconda
===============

.. note::

    Installing Anaconda3 will not prevent you from using Python 2.

    ``conda`` allows you to deploy multiple independent Python environments, at-will, under a single Anaconda installation. You may have trouble following along with this guide if you choose to install Anaconda2.


Go grab a copy of `Anaconda3 <https://www.continuum.io/downloads>`_ from Continuum Analytics, Inc. Be sure to select the installation medium appropriate for your operating system (Linux or OS X) and architecture (64-bit). The OS X GUI installer may cause side-effects, such as changing permissions of files in your home directory to ``root:wheel``, or mistakenly creating a system-wide installation under ``/anaconda`` instead of your personal home directory. To avoid this situation perform a command-line installation instead.

Follow the installation instructions for your platform provided on the download page. Before moving on to the next step, open a new terminal window, and run ``conda`` to verify your terminal session can find it.


Configure Conda
===============

In order to install packages directly from the AstroConda repository, you will need to configure Anaconda to do so. This will permanently add the repository to Conda's search path. Be aware that adding additional `anaconda.org <https://anaconda.org>`_ or direct-url repositories may affect the stability of AstroConda's run-time environment.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc


Install AstroConda
==================

Standard Installation (without IRAF)
------------------------------------

Now that Conda is configured to pull from our repository, you may go ahead and install the ``stsci`` metapackage. The example below generates a new conda environment named "astroconda", however, this naming convention is merely a suggestion. Feel free to use a name that works best for you.

.. code-block:: sh

    $ conda create -n astroconda stsci

This will prompt you to confirm the installation of all the STScI packages available in AstroConda. After they are installed, the following command "activates" the astroconda environment, making these packages available to you.

.. code-block:: sh

    $ source activate astroconda

.. note::

    Though it is repeated a lot in examples, ``source activate astroconda`` only needs to be run once per terminal session. Running this command ensures subsequent commands will take effect only in the ``astroconda`` environment, keeping your system organized.

    To deactivate the ``astroconda`` environment, close your terminal window or run ``source deactivate``.


.. _iraf_install:

Legacy Installation (with IRAF)
-------------------------------------


The developers of AstroConda have limited resources to support :abbr:`IRAF (Image Reduction and Analysis Facility)`, but users that require the ability to run IRAF and PyRAF tasks may want to install it through AstroConda. For help with many issues that come up during installation or use, please visit the `PyRAF FAQ <http://www.stsci.edu/institute/software_hardware/pyraf/pyraf_faq>`_. If you are running Linux be sure to visit `this FAQ entry <faq.html#in-linux-how-do-i-install-iraf-s-32-bit-dependencies>`_ for a quick guide to installing IRAF's 32-bit dependencies.

.. attention::

  Usage of IRAF currently requires running in a Python 2.7 environment.
  The instructions below will install IRAF into a separate, Python 2.7,
  environment regardless of your default Python version or which environments
  you've created previously.

  This will keep your IRAF environment separate from your other day-to-day
  environments, which will facilitate updating only one or the other, and allow
  easier transition off in the event of deprecation.  Simply ``source activate iraf27``
  for iraf work and ``source activate astroconda`` for day-to-day use.

.. code-block:: sh

    $ conda create -n iraf27 python=2.7 iraf pyraf stsci

Then, just as with the default installation, it is necessary to activate the environment to make its commands and packages available.

.. code-block:: sh

    $ source activate iraf27

Fine-tuning the Installation
============================

If you are short on hard drive space, have a slow internet connection, or are simply not interested in installing *everything but the kitchen sink*; please feel free to peruse the `manifest <http://ssb.stsci.edu/astroconda>`_ and install a custom mix of packages tailored to your needs.

.. code-block:: sh

    $ conda create -n astroconda [package [package ...]]
    $ source activate astroconda

Installing Other Packages
=========================

AstroConda provides a suite of packages that are known to work well together and are supported by engineers from STScI. However, being built on top of the widely-used ``conda`` tools for managing Python environments, AstroConda also supports the installation of additional 3rd-party packages.

Full documentation of the ``conda`` tool is available from Continuum Analytics, Inc., its creators and maintainers: http://conda.pydata.org/docs/using/index.html. However, we have provided a brief explanation of 3rd-party package installation below for quick reference.

For scientific packages available through Anaconda, installation is as simple as:

.. code-block:: sh

    $ source activate astroconda
    $ conda install name_of_pkg

Often, the easiest way to see if the package is available through Anaconda is to try installing it. The full list of available packages is here: http://repo.continuum.io/pkgs/.

The Python-standard tool ``pip`` is also available to install packages distributed through the Python Package Index (PyPI):

.. code-block:: sh

    $ source activate astroconda
    $ pip install name_of_pkg

.. rubric:: Footnotes

.. [#archnote] Intel x86_64 architecture
