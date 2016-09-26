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


header = """
Release Notes
=============

Individual release notes for packages can be found on their individual
pages, linked below.

"""

item = """
-  `{} <{}>`__
"""

def any_releases(url):
    no_release_msg = b"<h3>There aren\xe2\x80\x99t any releases here</h3>"

    if no_release_msg in urlopen(url).read():
        return False

    return True

def pull_release_notes(org, outfile):
    with open(outfile, 'w+') as mdout:
        # Write header (main title)
        print(header, file=mdout)

        # Sort repositories inline alphabetically, because otherwise its seemingly random order
        for repository in sorted(list(org.iter_repos()), key=lambda k: k.name):

            release_url = repository.html_url + '/releases'

            if not any_releases(release_url):
                continue

            print(item.format(repository.name.upper(), release_url), file=mdout)


def generate_release_notes():
    owner = 'spacetelescope'
    org = github3.organization(owner)

    outfile = os.path.join('source', 'release_notes.rst')

    try:
        pull_release_notes(org, outfile)
    except GitHubError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    generate_release_notes()
