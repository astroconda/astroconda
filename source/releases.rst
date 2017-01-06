Pipeline Releases
#################

.. note::

    - Python 2.x.x is not supported.
    - 32-bit operating systems are not supported.


Installation
============

To install a STScI pipeline release, use the following format:

.. code-block:: sh

    conda create -n [custom_env_name] --file [URL]
    source activate [custom_env_name]


Example
-------

.. code-block:: sh

    conda create -n demo_2016.1 \
        --file http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-linux-py35.2.txt
    source activate demo_2016.1

The URL used here will not be updated to reflect the latest iteration available. Please consult the :ref:`files` section to ensure you are installing the correct release.


.. _files:

File URLs
=========

Select the URL that matches your intended platform and environment.

HST Data Processing (HSTDP)
---------------------------

*HSTDP* was previously known as *OPUS*.

2016.1
++++++

========  ======  ===
PLATFORM  Python  URL
========  ======  ===
Linux     3.5     http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-linux-py35.2.txt
OS X      3.5     http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-osx-py35.2.txt
========  ======  ===

2016.2
++++++

========  ======  ===
PLATFORM  Python  URL
========  ======  ===
Linux     3.5     http://ssb.stsci.edu/conda/hstdp-2016.2/hstdp-2016.2-linux-py35.2.txt
OS X      3.5     http://ssb.stsci.edu/conda/hstdp-2016.2/hstdp-2016.2-osx-py35.2.txt
========  ======  ===

Release Schema
==============

If you wish to write shell scripts to manage your local pipeline installations, this may be of interest to you:

.. code-block:: sh

    RELEASE_HOME=http://ssb.stsci.edu/conda

    #               hstdp 2016  1
    #               ^     ^     ^
    RELEASE_PARENT=$NAME-$YEAR.$BUILD

    #                              linux     py35            2
    #                              ^         ^               ^
    RELEASE_CHILD=$RELEASE_PARENT-$PLATFORM-$PYTHON_VERSION.$ITERATION.txt
