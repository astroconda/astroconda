******************
Contributing Guide
******************


.. attention::

    A `GitHub <https://github.com>`_ account is required to begin contributing to AstroConda


Guidelines
==========

.. attention::

    The following packaging guidelines are subject to change at any time.

    - Please be respectful when commenting on pull-requests or issues.
    - If your contribution is not accepted into AstroConda, as a general courtesy, you will be given a clear and concise reason.
    - As a contributor you may not claim exclusive rights to a particular recipe.
    - You are free to maintain a recipe in AstroConda by issuing regular pull requests.
    - Everyone is welcome to improve upon recipes so long as the changes do not introduce packaging conflicts.
    - Abandoned recipes may be moved into the ``deprecated`` directory at any time without warning. (i.e. The package no longer compiles, has been obsoleted, or presents a conflict that cannot be resolved, etc).
    - Packages derived from ``deprecated`` recipes will remain available in AstroConda for historical purposes (i.e. to preserve backwards compatibility).

Bugs, questions, and requests
=============================

Please open a new issue or send us a pull request for bugs, feedback, questions, or enhancements. 

*  For documentation issues use the [astroconda issue tracker](https://github.com/astroconda/issue)
*  For recipie issues, use the [astroconda-contrib issue tracker](https://github.com/astroconda-contrib/issue)


Adding a recipe to astroconda-contrib
=====================================

In this example we will be adding a new recipe to the AstroConda repository for `sympy <http://sympy.org>`_, the
symbolic mathematics library.

Navigate to the `astroconda-contrib <https://github.com/astroconda/astroconda-contrib>`_ repository on GitHub, login, and create a fork (or click `here <https://github.com/astroconda/astroconda-contrib/fork>`_ to have your fork created automatically).

Now that you have a fork of astroconda-contrib, go ahead and clone it to your system:

.. code-block:: sh

    git clone https://github.com/[Your_Account]/astroconda-contrib
    cd astroconda-contrib


To get started adding our recipe, create a new branch and name it ``sympy-contrib``:

.. code-block:: sh

    git checkout -t -b sympy-contrib

Git will automatically switch your branch from ``master`` to ``sympy-contrib`` as denoted by the following output:

.. code-block:: sh

    Branch sympy-contrib set up to track local branch master.
    Switched to a new branch 'sympy-contrib'

If you have taken the liberty of looking around the astroconda-contrib directory, you will have noticed a bunch of directories are sitting in there all named by-package. So let's keep things simple and straight forward. Go ahead and create a directory and name it
``sympy``, and proceed inside:

.. code-block:: sh

    mkdir sympy
    cd sympy

.. note::

    This is not an Anaconda packaging tutorial. For more information about creating recipes from scratch, please refer to the `conda-build documentation <http://conda.pydata.org/docs/build_tutorials/pkgs2.html>`_.

    **Hint:** Investigate the contents of the recipes in astroconda-contrib. For most cases, copying an existing recipe and changing its values will suffice.

Copy the contents of the ``astroconda-contrib/template`` recipe.  Three files ``bld.bat``, ``build.sh``, and ``meta.yaml`` will be copied to your working directory:

.. code-block:: sh

    cp ../template/* .


Go ahead and open ``meta.yaml`` with your favorite plain-text editor:

.. caution::

    It is *highly recommended* that you enable "tabs to spaces" for your editor. Tab widths are unpredictable and may
     cause Conda's YAML parser to fail.

.. code-block:: sh

    vim meta.yaml


The general structure of the file is as follows:

.. code-block:: yaml

    # These directives are commented here due to Pygments
    # failing to parse this section of code.
    # ... They are not commented in the real file.

    #{% set name = '' %}
    #{% set version = '' %}
    #{% set number = '0' %}

    about:
        # Package homepage
        home:
        # Package license
        license:
        # A brief description
        summary:

    package:
        # Define these values above
        name: {{ name }}
        version: {{ version }}

    build:
        # Define this value above
        number: {{ number }}

    source:
        fn: {{ name }}-{{ version }}.tar.gz
        url: http://example.com/example/{{ name }}-{{ version }}.tar.gz

    requirements:
        build:
        # Dependencies required at BUILD-TIME go here
        - setuptools
        - python x.x
        run:
        # Dependencies required at RUN-TIME go here
        # - ...

    #test:
    #   imports:
    #   # - (e.g. a_python_module)
    #
    #   commands:
    #   # - (e.g. program --help)


First, let's fill in the blanks. Modify the JINJA2 template markers for ``name``, ``version``:

.. code-block:: none

    {% set name = 'sympy' %}
    {% set version = '1.0' %}


Fill in the ``about`` section with relevant information regarding the package:

.. code-block:: yaml

    about:
        home: http://sympy.org
        license: GPL
        summary: Python library for symbolic mathematics


Next, modify the ``source`` section's ``url`` so that it points to ``sympy``'s source archive (on the internet):

.. code-block:: sh

    source:
        fn: {{ name }}-{{ version }}.tar.gz
        url: https://github.com/{{ name }}/{{ name }}/releases/download/{{ name }}-{{ version }}/{{ name }}-{{ version }}.tar.gz


What's with the never-ending stream of bracket encapsulated keywords, you ask? Conda uses JINJA2, a basic template system that provides basic string interpolation within recipes. This comes in handy if, let's say, you decide to build a more recent version of ``sympy``, you need only modify the first two variable definitions in this file (assuming the URL structure has not changed).

The ``requirements`` section may be confusing to some, so let's clarify the distinction between ``build`` and ``run`` before diving in. The ``build`` section defines Conda packages required at compile-time (i.e. ``python setup.py install``), whereas the ``run`` section lists Conda packages required at install-time (i.e. ``conda install [package]``).

As recipe maintainer the method used to dependency discover is that of trial and error. For many Python packages obtained via PyPi, it is easy enough to visually examine ``setup.py`` or ``requirements.txt`` to get a good idea of the recipes you need to depend on. Some package may require several iterations of executing ``conda-build`` and returning to your recipe in the editor to append more packages.

As we can see below, ``sympy`` requires ``mpmath``, ``setuptools`` and ``python`` to *build* the recipe, but only ``mpmath`` and ``python`` to *run it* successfully after installation:

.. code-block:: yaml

    requirements:
        build:
        - mpmath
        - setuptools
        - python x.x
        run:
        - mpmath
        - python x.x

What does the ``x.x`` imply exactly? This instructs ``conda-build`` *not* to proceed unless ``python=[version]`` has been issued as an argument on the commandline. If ``x.x`` is omitted here, the recipe will choose the version of Python currently active in your environment. In most cases it is best to be explicit rather than implicit when it comes to defining version requirements in Conda.

The ``test`` section defines few useful lists, ``imports``, ``commands``, and ``requires``. While these are not *required* to be used in any given recipe, we do use them in AstroConda. The ``imports`` section is a list of Python module imports, the ``commands``
are executed in a basic shell environment, and finally ``requires`` defines any extraneous packages to be installed into the environment before running the tests.

.. code-block:: yaml

    test:
        imports:
            - sympy

        #commands:
        #   - no shell commands to execute

        #requires:
        #   - does not require any extra testing-related packages

If ``sympy`` provided a commandline utility named ``sympy-show``, you would use the ``commands`` section to verify the utility's functionality. A simple example of this would be to output a usage statement.

.. code-block:: sh

    test:
        # ...
        commands:
            - sympy-show --help

If a program returns greater than zero ``conda-build`` will fail as if it observed an error. Not all programs return zero after issuing ``--help`` (or an equivalent argument). Due to this, you may need to omit this style of test.

It will not hurt to keep the ``commands`` section populated but disabled with a note describing why it doesn't work. Others will find this information useful. Given this scenario, the optimal approach would be to contact the developers and plead with them to
normalize the exit value.


Below is our ``sympy`` final recipe. Despite the overwhelming use of JINGA2 in our example, things are looking pretty streamlined.

.. code-block:: none

    {% set name = 'sympy' %}
    {% set version = '1.0' %}

    about:
        home: http://sympy.org
        license: GPL
        summary: Python library for symbolic mathematics

    source:
        fn: {{ name }}-{{ version }}.tar.gz
        url: https://github.com/{{ name }}/{{ name }}/releases/download/{{ name }}-{{ version }}/{{ name }}-{{ version }}.tar.gz

    requirements:
        build:
        - mpmath
        - setuptools
        - python x.x
        run:
        - mpmath
        - python x.x

    test:
        imports:
            - sympy


The ``template`` directory copied earlier in this tutorial contains two basic python build scripts for both \*Nix (``build.sh``) and Windows (``bld.bat``), and is coincidentally compatible with the example we're using here. Not all Python packages (especially Makefile-based packages) will compile successfully using this "one-liner" template. Always refer to the ``INSTALL`` file or equivalent documentation for the program you are attempting to compile to learn more about what the package expects from the end-user at compile-time.

Before we can issue a pull request on GitHub, we first ensure it builds, tests, and installs properly on our local system. To do this we need to change our directory to one level above the recipe.

.. code-block:: sh

    cd ..
    # i.e. /path/to/astroconda-contrib

Now run ``conda-build`` to compile our ``sympy`` recipe into a Conda package. In the example below we are building against
Python 3.5:

.. code-block:: sh

    conda-build -c http://ssb.stsci.edu/astroconda --skip-existing --python=3.5 sympy

That's probably a bit more involved than you thought. Let's break it down. We issue ``-c [URL]`` which instructs the build to utilize the AstroConda channel while checking for package dependencies (i.e. the recipe's ``requirements`` section). Secondly, we issue ``--skip-existing`` to prevent ``conda-build`` from rebuilding dependencies discovered in the local astroconda-contrib directory. That is to say, if a package defined as a requirement exists remotely, it will then download and install it, rather than rebuild it from scratch. ``--python=`` is self-explanatory, and the final argument is the name of the recipe(s) we intend to build.

At this point, if the build was successful, our Conda package (a bzipped tarball) called ``sympy-1.0-py35_0.tar.bz2`` is emitted to ``/path/to/anaconda/conda-bld/[os-arch]/``. This directory is a local Conda package repository.

To install this new ``sympy`` package and interact with it ourselves you could run the following:

.. code-block:: sh

    conda create -n sympy_test --use-local sympy
    source activate sympy_test

Then manually verify the package is working:

.. code-block:: sh

    python

And checking it out for yourself:

.. code-block:: python

    >>> import sympy
    >>> sympy.__file__
    '/path/to/anaconda/envs/sympy_test/lib/python3.5/site-packages/sympy/__init__.py'

Now that you have verified the recipe is fully functional and are happy with the outcome, it's time to create a pull request against astroconda-contrib main repository.

Push your ``sympy-contrib`` branch up to your fork on GitHub:

.. code-block:: sh

    git push origin sympy-contrib


It is recommended that you familiarize yourself with GitHub pull requests before proceeding (see: `tutorial <https://help.github.com/articles/using-pull-requests/>`_).

Using GitHub, you will want to browse to your ``astroconda-contrib`` fork, select the ``sympy-contrib`` branch from
the drop-down menu (the default will read: "Branch: master", next to a black downward-pointing caret). Once selected, click the large green button labeled: "New pull request".

From here, you may wish to edit the title of your pull request and add initial comments or notes regarding what you have done, or list any work that may still need to be done. After submitting your pull request, a member of the Science Software Branch at STScI, or fellow contributors will review the requested changes, ask questions, offer feedback or advice.

At this point if everything appears to be in order your recipe will likely be merged, built, and incorporated into AstroConda!
