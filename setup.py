# -*- coding: utf-8 -*-

'''
setup for djvocab

Created on  2019-02-14

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2019 The Presidents and Fellows of Harvard College. All rights reserved.
@license: GPL v2.0
'''

import re
from setuptools import setup, find_packages


def getVersion():
    """
    Retrieve the version number from the __init__ file
    """
    version = '0.0.0'
    with open('djvocab/__init__.py', 'r') as f:
        contents = f.read().strip()

    m = re.search(r"__version__ = '([\d\.]+)'", contents)
    if m:
        version = m.group(1)
    return version


setup (
    name="djvocab",
    version=getVersion(),
    author='Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>',
    author_email='aaron_kitzmiller@harvard.edu',
    description='Vocabulary model that can be used by other models',
    license='LICENSE',
    include_package_data=True,
    url='https://github.com/harvardinformatics/djvocab',
    packages=find_packages(),
    long_description='Vocabulary model that can be used by other models',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires = [
        'Django==2.1.7',
    ],
)
