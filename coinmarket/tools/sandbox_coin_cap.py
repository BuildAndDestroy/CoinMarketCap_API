#!/usr/bin/env python3
"""API client to pull cryptocurrency data from live exchange rates.

    Copyright (C) 2020  Mitch O'Donnell devreap1@gmail.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import argparse
import csv
import glob
import json
import urllib

import pkg_resources

import prettytable


def display_version() -> str:
    """Display the version of CoinMarketCap_API installed."""
    __version__ = pkg_resources.require('CoinMarketCap')[0].version
    print(__version__)


def display_license() -> str:
    """Display the micro license and point to the full license."""
    description = __doc__
    legal_statement = '\ncoinmarketcap_api.py Copyright (C) 2020  Mitch O\'Donnell\n\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.\n\nPlease read the full LICENSE file.\n'
    print(description, legal_statement)


def parse_arguments() -> tuple:
    """Give options for user input."""
    url = 'https://sandbox-api.coinmarketcap.com/'
    epilog = f'[*] Tool used for sandbox working with the sandbox environment.\n[*] {url}'
    parser = argparse.ArgumentParser(epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-c', '--coins', action='append', type=lambda coin_and_portfolio_value: coin_and_portfolio_value.lower().split('='), nargs='*', dest='coins',
                        help='Provide coin names with/without the amount of coin in your wallet.\nExample: \n-c Bitcoin=10 eos ethereum=5\n-c bitcoin')
    parser.add_argument('-f', '--format', action='store_true',
                        help='Format dictionaries into a table.')
    parser.add_argument('-s', '--sort', action='store_true',
                        help='Sort coins alphebetically or highest US dollar amount.')
    parser.add_argument('-o', '--output', action='store_true',
                        help='Send portfolio to a file in .csv format.\nMust use with --coins.')
    parser.add_argument('-i', '--input', action='store_true',
                        help='Import a portfolio.csv file for formatting.')
    parser.add_argument('-L', '--License', action='store_true',
                        help='Print out the micro license for this software.\nSee LICENSE file for full license.')
    parser.add_argument('-V', '--Version', action='store_true',
                        help='Print out the current version of coin_market installed.')

    subparsers = parser.add_subparsers(help='commands', dest='command')

    cryptocurrency_parser = subparsers.add_parser('cryptocurrency', help='Use the cryptocurrency endpoint.')
    cryptocurrency_parser.add_argument('--map', action='store_true', help='Use the cryptocurrency/map API call.')
    cryptocurrency_parser.add_argument('--info', action='store_true', help='Use the cryptocurrency/info API call.')
    cryptocurrency_parser.add_argument('--listings-latest', action='store_true', help='Use the cryptocurrency/listings/latest API call.')
    cryptocurrency_parser.add_argument('--listings-historical', action='store_true', help='Use the cryptocurrency/listings/historical API call.')
    cryptocurrency_parser.add_argument('--quotes-latest', action='store_true', help='Use the cryptocurrency/quotes/latest API call.')
    cryptocurrency_parser.add_argument('--quotes-historical', action='store_true', help='Use the cryptocurrency/quotes/historical API call.')
    cryptocurrency_parser.add_argument('--market-pairs-latest', action='store_true', help='Use the cryptocurrency/market/pairs/latest API call.')
    cryptocurrency_parser.add_argument('--ohlcv-latest', action='store_true', help='Use the cryptocurrency/ohlcv/latest API call.')
    cryptocurrency_parser.add_argument('--ohlcv-historical', action='store_true', help='Use the cryptocurrency/ohlcv/historical API call.')
    cryptocurrency_parser.add_argument('--price-performance-stats-latest', action='store_true', help='Use the cryptocurrency/price/performance/stats/latest API call.')

    exchange_parser = subparsers.add_parser('exchange', help='Use the exchange endpoint.')
    exchange_parser.add_argument('--map', action='store_true', help='Use the /v1/exchange/map API call.')
    exchange_parser.add_argument('--info', action='store_true', help='Use the /v1/exchange/info API call.')
    exchange_parser.add_argument('--listings-latest', action='store_true', help='Use the /v1/exchange/listings/latest API call.')
    exchange_parser.add_argument('--listings-historical', action='store_true', help='Use the /v1/exchange/listings/historical API call.')
    exchange_parser.add_argument('--quotes-latest', action='store_true', help='Use the /v1/exchange/quotes/latest API call.')
    exchange_parser.add_argument('--quotes-historical', action='store_true', help='Use the /v1/exchange/quotes/historical API call.')
    exchange_parser.add_argument('--market-pairs-latest', action='store_true', help='Use the /v1/exchange/market-pairs/latest API call.')

    global_metrics_parser = subparsers.add_parser('global-metrics', help='Use the global-metrics endpoint.')
    global_metrics_parser.add_argument('--latest', action='store_true', help='Use the /v1/global-metrics/quotes/latest API call.')
    global_metrics_parser.add_argument('--historical', action='store_true', help='Use the /v1/global-metrics/quotes/historical API call.')

    tools_parser = subparsers.add_parser('tools', help='Use the tools endpoint.')
    tools_parser.add_argument('--price-conversion', action='store_true', help='Use the /v1/tools/price-conversion API call.')

    blockchain_parser = subparsers.add_parser('blockchain', help='Use the blockchain endpoint.')
    blockchain_parser.add_argument('--latest', action='store_true', help='Use the /v1/blockchain/statistics/latest API call.')

    fiat_parser = subparsers.add_parser('fiat', help='Use the fiat endpoint.')
    fiat_parser.add_argument('--map', action='store_true', help='Use the /v1/fiat/map API call.')

    partners_parser = subparsers.add_parser('partners', help='Use the partners endpoint.')
    partners_parser.add_argument('--listings-latest', action='store_true', help='Use the /v1/partners/flipside-crypto/fcas/listings/latest API call.')
    partners_parser.add_argument('--quotes-latest', action='store_true', help='Use the /v1/partners/flipside-crypto/fcas/quotes/latest API call.')

    key_parser = subparsers.add_parser('key', help='Use the key endpoint.')
    key_parser.add_argument('--info', action='store_true', help='Use the /v1/key/info API call.')

    args = parser.parse_args()
    return args


def main() -> None:
    """Pull the full list of coins in JSON format.

    If no arguments present, return all dictionaries.
    If arguments, return dictionaries with/without formatting.
    """
    print('Coming soon!')
    args = parse_arguments()
    print(args)


if __name__ == '__main__':
    main()
