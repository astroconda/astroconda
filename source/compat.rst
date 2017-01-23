*********************
Compatibility Notices
*********************

As the Conda package ecosystem evolves and third-party software updates are released by Continuum and other providers, this may interfere with the stability of other codebases, such as STScI's software. This page will proactively chronicle such events as they occur as well as provide workarounds to these issues.

If you spot a compatibility problem not listed here please let us know by sending an email to help@stsci.edu

.. note::

  **You may be effected by an issue if you have updated your AstroConda environment on or after the dates listed in each section below.**


12/23/2016
==========

AstroPy v1.3 fully deprecated calls to ``astropy.io.fits.new_table``. The following packages are known to be incompatiable with this release:

  * ``calcos =< 3.1.8`` - Bugfix pending
  * ``costools <= 1.2.1`` - Bugfix pending
  * ``fitsblender =< 0.2.6`` - 0.3.0 released (01/17/2017)

Recommended user actions:

  * Upgrade ``fitsblender`` to version 0.3.0 (i.e. ``conda update fitsblender``)

Alternative user actions:

  * Downgrade ``astropy`` to version 1.2.1 (i.e. ``conda install astropy=1.2.1``)

