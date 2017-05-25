#########################
Updating a Software Stack
#########################

Conda, will not automatically update unless a newer version of a package is detected during a routine package installation. Suffice to say, unless you keep your packages up to date with ``conda update``, the packages installed in your environment will remain static.


There are few simple ways to update packages obtained from AstroConda:

Updating via Metapackage
========================

.. code-block:: sh

    $ conda update -n astroconda stsci

This is best used by individuals that favor software stability over receiving the "bleeding edge". Remember, updating the ``stsci`` package only effects packages part of the **official release** of our software. Packages provided by the AstroConda channel, but are not controlled by the ``stsci`` package **will not receive updates**. This is true for other packages as well (e.g. ``stsci-hst``, ``stsci-data-analysis``, etc).

To clarify what this does, if the ``stsci`` package (used to create your environment) has not been updated by STScI to accommodate recently added packages, or newer versions of those packages, nothing will be updated in your environment on behalf of ``stsci``. In general, to receive interim bug fix releases please consider updating all packages, or individual packages of interest.

Updating All Packages
=====================

.. code-block:: sh

    $ conda update -n astroconda --all

This will apply updates to all packages installed in your ``astroconda`` environment [1]_ regardless if they were installed via AstroConda, Continuum Analytics, Inc., or other third party channels defined within your ``$HOME/.condarc``.

(`ref <http://conda.io/docs/using/pkgs.html#package-update>`__)


Updating Individual Packages
============================
.. code-block:: sh

    $ conda update -n astroconda <name_of_pkg>

If you are interested in receiving updates for a particular package, then this method is for you. Be aware that packages may depend on other packages, so the total list of package updates returned by this command will vary.


Updating Conda
==============

.. code-block:: sh

    $ source deactivate
    $ conda update --all

Keeping AstroConda packages up to date is important, but not nearly as important as keeping your 'root' (i.e. the base installation) updated as well. Conda is like any other software project and it requires periodic refreshing to stay current with the latest changes. Failing to do this can, over time, cause side-effects such as, the inability to upgrade, install, remove, or search for packages.

Updating extremely old releases of Conda to the latest version have been known to break the 'root' environment due to a variety of API changes in the code. There is not much STScI can do about this as Conda itself is not our product, however if this happens to you, reinstalling the latest release of Miniconda or Anaconda, then regenerating your AstroConda software environment is the fastest way to resolve the problem. Refer to the `FAQ <faq.html#how-do-i-reinstall-miniconda>`_ for more details.


.. rubric:: Footnotes

.. [1] (STScI-Specific) "Updating All Packages" now assumes the role of "SSBX" in the AstroConda distribution model.
