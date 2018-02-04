#!/usr/bin/env python
"""
    To install, run:
    sudo pip install .
    If upgrading, run:
    sudo pip install --upgrade .
"""

from setuptools import setup

__version__ = '2.3.5-import_csv'
packages = ['coinmarket']
commands = ['coin_market = coinmarket.coinmarketcap_api:main']

setup(
    name                ='CoinMarketCap',
    version             =__version__,
    description         = 'Coin exchange API client to pull exchange data.',
    author              = 'Mitch O\'Donnell',
    author_email        = 'devreap1@gmail.com',
    packages            = packages,
    url                 = '',
    license             = open('LICENSE').read(),
    install_requires    = ['prettytable'],
    entry_points        = {'console_scripts': commands},
    prefix              = '/opt/CoinMarketCap',
    long_description    = open('README.md').read()
)
