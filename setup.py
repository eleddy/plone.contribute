# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = \
    read('README.rst') + \
    read('docs', 'HISTORY.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='plone.contribute',
    version=version,
    description="A simple plugin to collect contributor agreements for Plone core",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='Caipirina Sprinters',
    author_email='plone-users@lists.sourceforge.net',
    url='http://githib.com/collective/plone.contribute',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plone'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'five.pt',
        'Pillow',
        'Plone',
        'plone.api',
        'plone.app.caching',
        'plone.app.dexterity',
        'plone.app.theming',
        'setuptools',
        'requests', # for github integration
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'pep8',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'setuptools-flakes',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
