#!/usr/bin/env python3
"""Library for everything about CoinMarketCap_API."""

import pkg_resources


def display_version() -> str:
    """Display the version of CoinMarketCap_API installed."""
    __version__ = pkg_resources.require('CoinMarketCap')[0].version
    print(f'Version: {__version__}')


def display_license() -> str:
    """Display the micro license and point to the full license."""
    description = __doc__
    legal_statement = '\ncoinmarketcap_api.py Copyright (C) 2020  Mitch O\'Donnell\n\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.\n\nPlease read the full LICENSE file.\n'
    print(description, legal_statement)
