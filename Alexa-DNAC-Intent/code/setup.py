# -*- coding: utf-8 -*-
"""
Meraki API Setup module.
"""

from os import path
from codecs import open as codecs_open
from setuptools import setup, find_packages
from meraki_api import __version__

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs_open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='meraki_api',
    version=__version__,
    description='Meraki Dashboard API wrapper.',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/guzmonne/meraki_api',
    # Author details
    author='Guzmán Monné',
    author_email='guzmonne@hotmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    # Github archive
    download_url=(
        "https://github.com/guzmonne/meraki_api/archive/"
        + __version__
        + ".tar.gz"
    ),
    # What does your project relate to?
    keywords='api development',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #   'test': ['coverage'],
    #},
)
