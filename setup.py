#!/usr/bin/env python
"""
    To install, run:
    sudo pip install .
    If upgrading, run:
    sudo pip install --upgrade .
"""

from setuptools import setup

__version__ = '3-0-beta'
packages = ['coinmarket',
            'coinmarket.tools',
            'coinmarket.lib'
            ]
commands = ['sandbox_coin_cap = coinmarket.tools.sandbox_coin_cap:main']

setup(
    name                ='CoinMarketCap',
    version             =__version__,
    description         = 'API client to pull CoinMarketCap data.',
    author              = 'Mitch O\'Donnell',
    author_email        = 'devreap1@gmail.com',
    packages            = packages,
    url                 = 'https://github.com/BuildAndDestroy/CoinMarketCap_API',
    license             = open('LICENSE').read(),
    install_requires    = [
                            'prettytable',
                            'requests'
                            ],
    entry_points        = {'console_scripts': commands},
    prefix              = '/opt/CoinMarketCap',
    long_description    = open('README.md').read()
)
