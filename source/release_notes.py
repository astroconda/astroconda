#!/usr/bin/env python
from __future__ import print_function

import os
import math
from collections import OrderedDict

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    import github3
    from github3 import organization
    from github3 import GitHubError
except ImportError:
    print('github3.py required.')
    print('pip install https+git://github.com/sigmavirus24/github3.py')
    exit(1)

from package_manifest import ARCHITECTURE, get_repodata


header = """
Release Notes
=============

Individual release notes for packages can be found on their individual
pages, linked below.

"""

item = """
-  `{} <{}>`__
"""

#-------------------------------------------------------------------------------

def any_releases(url):
    """Check if there are any releases in a given github release page

    Parameters
    ----------
    url: str
        URL of a valid github reposoitory release pages

    Returns
    -------
    any_releases: bool
        True if there are found releases, False otherwise

    """

    no_release_msg = b"<h3>There aren\xe2\x80\x99t any releases here</h3>"

    if no_release_msg in urlopen(url).read():
        return False

    return True

#-------------------------------------------------------------------------------

def pull_release_notes(org, outfile):
    """ Get urls for release notes for all astroconda packages

    Only repositories that are included in ANY astroconda distribution (linux or OSX)
    with tagged github releases will be included in the output release notes
    rst file.

    Parameters
    ----------
    org: github3 organization instance
        All repositories from this org will be parsed for releases
    outfile: str
        Filename to write urls to.

    """

    astroconda_packages = {item['name'] for arch in ARCHITECTURE for item in get_repodata(arch).values()}

    with open(outfile, 'w+') as mdout:
        # Write header (main title)
        print(header, file=mdout)

        # Sort repositories inline alphabetically, because otherwise its seemingly random order
        for repository in sorted(list(org.iter_repos()), key=lambda k: k.name):

            if not repository.name in astroconda_packages:
                continue

            release_url = repository.html_url + '/releases'

            if not any_releases(release_url):
                continue

            print(item.format(repository.name.upper(), release_url), file=mdout)

#-------------------------------------------------------------------------------

def generate_release_notes():
    """Main function to create the release_notes.rst pages
    """

    owner = 'spacetelescope'
    org = github3.organization(owner)

    outfile = os.path.join('source', 'release_notes.rst')

    try:
        pull_release_notes(org, outfile)
    except GitHubError as e:
        print(e)
        exit(1)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    generate_release_notes()
