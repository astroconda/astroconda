###############
Getting Started
###############

.. _getting_started_jump:

Installing Conda - The choice is yours
======================================

AstroConda is a third-party addon channel designed for use with the Conda package management system, so therefore in order to install software provided by our channel, you must first install a basic Conda environment on your system. This can be achieved in multiple ways (described below). Our channel's software is compatible with both of the ``2`` and ``3`` variants of Continuum Analytics, Inc.'s Miniconda and Anaconda distributions (i.e. Miniconda2, Miniconda3, Anaconda2, and Anaconda3).

Miniconda2 and Miniconda3 provide a bare-minimum Conda root environment with Python 2.7 or Python 3.x, respectively. (*Recommended*)

Anaconda2 and Anaconda3 are Continuum Analytics Inc.'s flagship products, and provide a full-featured Conda root environment as well as hundreds of useful tools, libraries, and utilities by default.

Both of Continuum's official distributions support a variety of operating systems and architectures, however the AstroConda channel specifically provides packages for Linux and Apple OS X running on x86_64 Intel/AMD processors. It is important to note Microsoft Windows is not supported at this time.

Now head over to **one** of the following sites and download a copy of the installer of your choice:

- Download `Miniconda <https://conda.io/miniconda.html>`_
- Download `Anaconda <https://www.continuum.io/downloads>`_ (OS X users should choose the command-line installer)

The installation method used for Miniconda and Anaconda are identical, however keep in mind the scripts are written in BASH (not SH), so therefore you *must* execute the installer using ``bash``:

.. code-block:: sh

    $ cd <download_directory_here>
    $ bash <install_script_here>

After the installation is complete double-check the bottom of ``~/.bash_profile`` to ensure Miniconda or Anaconda has been added to your ``PATH``. Otherwise, you will be unable to successfully complete this guide.

.. warning::

    Conda requires BASH, or a BASH-compatible shell in order to function correctly. If your default shell environment is not BASH (see also, :ref:`system_requirements`), please execute ``bash -l`` before proceeding.

    From this point forward any time you wish to use Conda's environment activation script (i.e. ``source activate <env_name>``), you will need to execute ``bash -l`` prior to doing so.


Verifying your Conda Environment
================================

Execute the command: ``which conda``

If the path to ``conda`` (i.e. ``/home/username/miniconda3/bin/conda``), is not returned, continue reading, otherwise skip ahead to :ref:`configure_astroconda_channel`.

If you answered ``Y`` or ``Yes`` when prompted during installation to place Miniconda or Anaconda in your ``PATH``, and ``which conda`` still does not return a path leading back to ``conda``, go ahead and execute ``source ~/.bash_profile``, then re-execute ``which conda``. If the path to ``conda`` appears, skip ahead to :ref:`configure_astroconda_channel`.

However, if you answered ``N`` or ``No`` when prompted, you will need to fix your ``PATH`` manually. If you installed Miniconda or Anaconda using the defaults selected by the installer, but are not sure what the directory is named, use the following command to find out:

.. code-block:: sh

    $ ls -d ~/*conda?
    #[example output]
    /home/username/miniconda3

Now append **one of the following** ``export`` commands that best matches the output of `ls -d` above to the bottom of ``~/.bash_profile`` using a plain-text editor:

.. code-block:: sh

    export PATH="~/miniconda/bin:$PATH"
    export PATH="~/miniconda3/bin:$PATH"
    export PATH="~/anaconda/bin:$PATH"
    export PATH="~/anaconda3/bin:$PATH"

At this point, to assume the new environment with ``conda`` in your ``PATH``, open a new terminal or execute ``source ~/.bash_profile`` and continue on to :ref:`configure_astroconda_channel`.

.. _configure_astroconda_channel:

Configure Conda to use the Astroconda Channel
=============================================

In order to install packages directly from the AstroConda channel you will need to append our URL to Conda's channel search path.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc

Be aware that indiscriminately adding channels to your configuration, be it from `anaconda.org <https://anaconda.org>`_ or via direct-URL can effect the stability of software packages in your run-time environment.

For example, if you add a channel found on anaconda.org because it contains a software package you're interested in, but it too provides the same software found in AstroConda, it's possible you may lose track of where packages are coming from. Or worse, the software you installed from the other channel was built incorrectly or did not account for a special case, so now the packages in your environment relying on this as a dependency could very well cease to function correctly.

If you decide to have multiple channels defined in your configuration and bugs begin to appear, it may be best to check their origin before issuing a support ticket to help@stsci.edu. ``conda list`` can be used to display such information about the packages installed in your environment.
