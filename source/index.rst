Welcome to AstroConda Channel's documentation!
==============================================

.. warning::
   **Astroconda is no longer supported by STScI; support ended on February 1st, 2023.** Users are encouraged to use `stenv <https://stenv.readthedocs.io/en/latest>`_ ``stenv`` provides a common environment for both the Hubble Space Telescope (HST) and the James Webb Space Telescope (JWST) pipelines and includes most commonly-used packages in Astroconda. Questions about this transition can be directed to the HST Help Desk: `hsthelp.stsci.edu <https://hsthelp.stsci.edu>`_
   
AstroConda is a free Conda channel maintained by the `Space Telescope Science Institute <http://www.stsci.edu/>`_ (STScI) in Baltimore, Maryland.  This channel provides tools and utilities required to process and analyze data from the Hubble Space Telescope (HST), James Webb Space Telescope (JWST), and others.

.. _system_requirements:

System Requirements
-------------------

    - 64-bit Intel/AMD processor (x86_64)
    - 64-bit Linux (glibc ≥ 2.12) or Mac OS X (≥ 10.7)
    - BASH or ZSH as your default shell environment (T/CSH is NOT supported)

Powered by Conda
----------------

Conda is an open-source software package management system provided and maintained by `Continuum Analytics <https://www.continuum.io/>`_.  Many software packages, provided both by Continuum and through third parties, are able to be quickly and easily installed using the Conda utility.  AstroConda serves as a third-party add-on channel to provide easy access to STScI's software packages.

- **New to conda**: :ref:`getting_started_jump`
- **Familiar with conda**: :ref:`configure_astroconda_channel`


.. note::  If you are using conda `4.3.30` or older, please upgrade to version `4.3.31` or newer before attempting to install or update any packages due to a bug in older versions that makes a large number of packages invisible and unable to be installed. Upgrading conda from this state may require two steps. The following commands will allow you to verify that the upgrade was successful.::

   $ source activate root
   $ conda --version
     conda 4.3.30
   $ conda update conda
   $ conda --version
     conda 4.3.31
   $ conda update conda
   $ conda --version
     conda 4.5.4 (Or whatever the latest version happens to be.)


To receive AstroConda announcements, or engage in general discussion, feel free to subscribe to our `mailing list <https://groups.google.com/forum/#!forum/astroconda>`_.


.. toctree::
   :maxdepth: 2

   getting_started
   installation
   updating
   further_reading
   releases
   compat
   faq
   contributing
   package_manifest
   release_notes
   resources
   disclaimer

