######
F.A.Q.
######


After "conda create -n ..." why does "source activate astroconda" fail?
============================================================================

Anaconda does not support CSH (C-Shell). Please switch to a POSIX-compatible shell (e.g. BASH, KSH, ZSH).

.. note::

    STScI will not maintain a separate codebase of Anaconda's backend ``conda`` in order to implement CSH support. Feel free to create an issue with the `developers <http://github.com/conda/conda/issues>`_.

I installed AstroConda into my Anaconda 'root' environment. What now?
=====================================================================

Please reinstall Anaconda from scratch. AstroConda uses ``source activate`` and ``source deactivate`` calls to
control your shell environment. The Anaconda 'root' environment **does not** use this feature, and thus, the packages you have installed there will not work properly.

To clarify, it is impossible to execute ``source activate root``. Installing AstroConda packages directly into the 'root' may cause Anaconda itself to be come unstable. In addition to this, removing packages from this environment is tedious and will likely break your Anaconda installation if you are not careful. *Reinstalling from scratch is the safest option.*

Why am I being prompted by NumPy/SciPy with a MKL 30-day trial warning?
=======================================================================

The ``root`` environment of your Anaconda installation is severely outdated (``<=2.4.0``) and suffers from a crippling bug introduced by the ``conda-3.19.x`` package.

It is possible to verify the version of Anaconda you have by running:

.. code-block:: sh

    $ conda info anaconda

The only solution is to update your Anaconda installation to the latest release:

.. code-block:: sh

    $ source deactivate
    $ conda update conda
    $ conda update anaconda

Next, update the ``astroconda`` environment to realign your packages with the ``root`` environment:

.. code-block:: sh

    $ conda update -n astroconda --all
    $ source activate astroconda

After doing this, the ``mkl`` 30-day trial warning will not be displayed while importing ``numpy``, ``scipy``, or any other package requiring ``mkl``.

How does AstroConda differ from Ureka?
======================================

Ureka and AstroConda both provide applications and libraries in binary form, however Ureka was a *one size fits all* distribution which included every package in one giant tarball. If an end-user only really wanted a small set of packages they were forced to install everything *and then some*. AstroConda is a *if the shoe fits wear it* distribution of packages. If an end-user needs ``HSTCAL``, for example, they can install ``HSTCAL`` and omit much of the rest of HST's software suite.

A *major difference* most people will appreciate is the sheer lack of shell scripts. Ureka's environment was controlled by several dozen independent scripts. What makes AstroConda different? For one, it is not controlled by user-executed scripts. Changes to the environment are applied by special (read: embedded) scripts that are executed automatically by ``source activate``, and the environment variables are unset with every ``source deactivate``. This allows you to switch between several different environments rapidly without needing to keep track of what is
defined in the environment.

How often are updates released?
===============================

Updates to (STScI) software will be released as bugs are identified and squashed. The ``stsci-*`` metapackages, for example, provide "releases" (i.e. a set of software used by our internal pipelines). After installing a release it is then possible to upgrade to the latest out-of-band packages by simply running:

``conda update -n astroconda --all``

Non-STScI software will be upgraded on an as-needed basis. See the `Contibuting Guide <contributing.html>`_ to learn more about asking for updates to existing packages.

What happened to SSBX?
======================

SSBX was a weekly release of STScI's software suite regardless of the stability of the codebase. This release was often times broken and caused issues for external users. SSBX has been rolled into AstroConda as out-of-band package updates. This offers a much better user experience, because as bugs are fixed, people will be able to upgrade without waiting until the following week.

What happened to SSBDEV?
========================

SSBDEV was a nightly snapshot release of STScI's software suite. This release was often times broken and caused issues for external users. Nightly snapshots are ***no longer available*** for use by the public. Updates to AstroConda will be made directly as existing software is improved and/or new software is released.

Why isn't IRAF installed by default?
====================================

IRAF is an extremely large software package. Not every developer or scientist requires it.

If you wish to use IRAF, simply install it :

``conda create -n iraf27 python=2.7 iraf pyraf stsci && source activate iraf27``

If you are already using AstroConda under a Python 2 environment, you may simply install IRAF/PyRAF into that environment:

``conda install -n astroconda iraf pyraf``

.. _iraf_python3:

Why is IRAF/PyRAF less functional under Python 3?
=================================================

The Python code in ``stsdas``, for example, is targeted specifically for Python 2.7 and earlier. If the demand for Python3 support under IRAF is great enough we may be able to pull our resources to accommodate the community. It is recommended to install IRAF into its own environment under Python 2.7:

``conda create -n iraf27 python=2.7 iraf pyraf stsci && source activate iraf27``

Why is IRAF 32-bit instead of 64-bit?
=====================================

Many of the IRAF tasks that we include with AstroConda are so old that they cannot be compiled as 64-bit executables without significant changes to the source code. Because of this restriction, we always build IRAF as a 32-bit program, even for our 64-bit distributions.

In Linux, how do I install IRAF's 32-bit dependencies?
------------------------------------------------------

Debian >=7, Ubuntu >=14.04
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    # If on Debian execute this first (not required on Ubuntu):
    sudo dpkg --add-architecture i386

    sudo apt-get update
    sudo apt-get install libc6:i386 libz1:i386 libncurses5:i386 libbz2-1.0:i386 libuuid1:i386 libxcb1:i386

RHEL/CentOS >=6, Fedora >=14
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    sudo yum install glibc.i686 zlib.i686 ncurses-libs.i686 bzip2-libs.i686 uuid.i686 libxcb.i686

Will AstroConda interfere with other scientific distributions (e.g. SciSoft)?
=============================================================================

**Probably**, however unlike Ureka, we do not impose any restrictions on your environment or issue compatibility warnings at run-time. It is your responsibility to maintain a functional shell environment so [insert scientific distribution here] does not conflict with your Anaconda installation.

Ds9 - Cannot select regions
===========================

The default edit mode is now ``None`` rather than ``Region``. To select ``Region`` as the default editing mode perform the steps listed here:

- Click ``Edit``
    - Click ``Preferences``
        - On the left pane, select ``Menus and Buttons``
        - On the right pane, click the ``Menu --`` drop-down menu beneath the ``Edit`` group
        - Select ``Region`` (default is ``None``)
    - Click the ``Save`` button at the bottom of the ``Preferences`` dialog box

