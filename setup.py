import os
from setuptools import setup, find_packages
from setuptools.command.install import install

import sys
sys.path.insert(0, 'source/')
#import release_notes
import package_manifest

class MyInstall(install):
    def run(self):
        install.run(self)
        #release_notes.generate_release_notes()
        package_manifest.generate_manifest()

setup(
    name = 'astroconda',
    version = '0.0.1',
    author = 'Joseph Hunkeler',
    cmdclass = {'install': MyInstall},
    install_requires = ['pypandoc', 'github3.py']
    )
