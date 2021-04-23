##########################
Selecting a Software Stack
##########################

A "stack" is a collection of software designed to target the various use cases of our end-users. The three officially supported stacks are as follows:

- :ref:`standard_install` provides:
    - The full compliment of STScI software and utilities
    - Python 2.7 or 3.x
- :ref:`iraf_install` provides:
    - The full compliment of STScI software and utilities
    - A IRAF/PyRAF environment
    - Python 2.7 only
- :ref:`pipeline_install_jump` provides:
    - The data processing environment used by STScI operations and instrument teams
    - Python 3.x only

.. _configure_astroconda_channel:


Configure Conda to use the Astroconda Channel
=============================================

In order to install packages directly from the AstroConda channel you will need to append our URL to Conda's channel search path.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc


.. _standard_install:

Standard Software Stack (without IRAF)
======================================

The package management system, Conda, is now configured to pull from our repository, so you may go ahead and install the ``stsci`` package. This package installs nearly all of the software provided by STScI in one shot.

The following example generates a new conda environment named "astroconda", however this naming convention is merely a suggestion. Feel free to use a name that works best for you.

.. code-block:: sh

    $ conda create -n astroconda python=3.7 stsci

After the installation is complete go ahead and activate the "astroconda" environment. This command only needs to be executed one time per terminal session.

.. code-block:: sh

    $ source activate astroconda

To deactivate the "astroconda" environment, close your terminal window or run:

.. code-block:: sh

    $ source deactivate


.. _iraf_install:

Legacy Software Stack (with IRAF)
=================================

.. raw:: html

  <b><font size="5" color="red">PLEASE NOTE: STScI will discontinue providing help desk support for IRAF starting October 1, 2019. Support may be sought thereafter via the IRAF forum <a href="https://iraf.net/forum/index.php">https://iraf.net/forum/index.php</a> or <a href="https://github.com/iraf-community/iraf">iraf-community</a> on Github.</font></b>

The maintainers of the AstroConda channel have limited resources to support :abbr:`IRAF (Image Reduction and Analysis Facility)`, but users that require the ability to run IRAF and PyRAF tasks may want to install it via AstroConda. For help with any issues that come up during installation or use, please visit the `PyRAF FAQ <http://www.stsci.edu/institute/software_hardware/pyraf/pyraf_faq>`_. **Linux users** please be sure to visit `this FAQ entry <faq.html#in-linux-how-do-i-install-iraf-s-32-bit-dependencies>`_ for a quick guide to installing IRAF's 32-bit dependencies.

The package management system, Conda, is now configured to pull from our repository, so you may go ahead and install the ``iraf-all`` package, as well as ``pyraf-all``, and finally ``stsci``. The ``stsci`` package installs nearly all of the software provided by STScI in one shot, however if you prefer a slimmed down IRAF/PyRAF experience, feel free to omit it.

Due to Python 3.x incompatibilities present in several tasks, it is recommended to install IRAF alongside Python 2.7.

The following example generates a new conda environment named "iraf27", however this naming convention is merely a suggestion, so please feel free to apply a name that works best for you.

.. code-block:: sh

    $ conda create -n iraf27 python=2.7 iraf-all pyraf-all stsci

After the installation is complete go ahead and activate the "iraf27" environment. This command only needs to be executed one time per terminal session.

.. code-block:: sh

    $ source activate iraf27

To deactivate the "iraf27" environment, close your terminal window or run:

.. code-block:: sh

    $ source deactivate


.. _pipeline_install_jump:

Pipeline Software Stack
=======================

Due to the nature of the pipeline software stack, the installation instructions have been consolidated under a separate section, :ref:`pipeline_install`.

