#!/usr/bin/env python3
"""Library for API calls.

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
import requests

import prettytable


class CoinMarketCapURL(object):
    """Build URL's for the api call to the environment."""

    def __init__(self, environment):
        self.api_url = self.environment(environment)

    def environment(self, environment):
        """Run a check for sandbox or production environment being requested"""
        if environment == 'sandbox':
            api_url = 'https://sandbox-api.coinmarketcap.com/v1'
        if environment == 'production':
            api_url = 'https://pro-api.coinmarketcap.com/v1'
        return api_url

    def endpoint_dictionary(self) -> dict:
        """Dictionary of each endpoint and the available directories."""
        endpoints_dict = {'/cryptocurrency': [
                                                '/map',
                                                '/info',
                                                '/listings/latest',
                                                '/listings/historical',
                                                '/quotes/latest',
                                                '/quotes/historical',
                                                '/market-pairs/latest',
                                                '/ohlcv/latest',
                                                '/ohlcv/historical',
                                                '/price-performance-stats/latest'
                                                ],
                          '/exchange': [
                                            '/v1/exchange/map',
                                            '/v1/exchange/info',
                                            '/v1/exchange/listings/latest',
                                            '/v1/exchange/listings/historical',
                                            '/v1/exchange/quotes/latest',
                                            '/v1/exchange/quotes/historical',
                                            '/v1/exchange/market-pairs/latest'
                                            ],
                          '/global-metrics': [
                                                '/v1/global-metrics/quotes/latest',
                                                '/v1/global-metrics/quotes/historical'
                                                ],
                          '/tools': [
                                        '/v1/tools/price-conversion'
                                        ],
                          '/blockchain': [
                                            '/v1/blockchain/statistics/latest'
                                            ],
                          '/fiat': [
                                        '/v1/fiat/map'
                                        ],
                          '/partners': [
                                            '/v1/partners/flipside-crypto/fcas/listings/latest',
                                            '/v1/partners/flipside-crypto/fcas/quotes/latest'
                                            ],
                          '/key': [
                                    '/v1/key/info'
                                    ],
                          }
        return endpoints_dict


    def generate_urls(self, endpoint, all_subparsers_requested) -> str:
        """"""
        endpoint_dictionary = self.endpoint_dictionary()
        possible_urls = []

        # This is a generator to check all possible URL's to call.
        for args in all_subparsers_requested:
            for key, value in endpoint_dictionary.items():
                if endpoint in key:
                    for index in value:
                        if args in index:
                            possible_urls.append(f'{self.api_url}{key}{index}')
        return possible_urls

    def get_sandbox_api_key(self) -> str:
        """If no API key is set, tell user where to get one."""
        url = 'https://sandbox.coinmarketcap.com/'
        return f'[*] No API Key is set.\n    Get your Sandbox API key at {url}'

    def get_prod_api_key(self) -> str:
        """If no API key is set, tell user where to get one."""
        url = 'https://pro.coinmarketcap.com/'
        return f'[*] No API Key is set.\n    Get your Production API key at {url}'


class UserArguments(object):
    """Cascade through user input"""
    def __init__(self, environment):
        self.environment = self.coinmarket_environment(environment)
        self.args = self.parse_arguments()

    def coinmarket_environment(self, environment):
        """Check the environment we are using to interface."""
        if environment == 'sandbox':
            return 'sandbox'
        elif environment == 'production':
            return 'production'
        else:
            raise ValueError('Expected "sandbox" or "production".') 

    def parse_arguments(self) -> tuple:
        """Give options for user input."""
        if self.environment == 'sandbox':
            url = 'https://sandbox-api.coinmarketcap.com/'
            epilog = f'[*] This tool is used for the coinmarketcap sandbox environment.\n[*] {url}'
        elif self.environment == 'production':
            url = 'https://pro-api.coinmarketcap.com'
            epilog = f'[*] This tool is used for the coinmarketcap Production environment.\n[*] {url}'
        parser = argparse.ArgumentParser(
            epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('your_api_key', help='Add your api key for the sandbox environment.')
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

        cryptocurrency_parser = subparsers.add_parser(
            'cryptocurrency', help='Use the cryptocurrency endpoint.')
        cryptocurrency_parser.add_argument(
            '--map', action='store_true', help='Use the cryptocurrency/map API call.')
        cryptocurrency_parser.add_argument(
            '--info', action='store_true', help='Use the cryptocurrency/info API call.')
        cryptocurrency_parser.add_argument(
            '--listings-latest', action='store_true', help='Use the cryptocurrency/listings/latest API call.')
        cryptocurrency_parser.add_argument(
            '--listings-historical', action='store_true', help='Use the cryptocurrency/listings/historical API call.')
        cryptocurrency_parser.add_argument(
            '--quotes-latest', action='store_true', help='Use the cryptocurrency/quotes/latest API call.')
        cryptocurrency_parser.add_argument(
            '--quotes-historical', action='store_true', help='Use the cryptocurrency/quotes/historical API call.')
        cryptocurrency_parser.add_argument(
            '--market-pairs-latest', action='store_true', help='Use the cryptocurrency/market/pairs/latest API call.')
        cryptocurrency_parser.add_argument(
            '--ohlcv-latest', action='store_true', help='Use the cryptocurrency/ohlcv/latest API call.')
        cryptocurrency_parser.add_argument(
            '--ohlcv-historical', action='store_true', help='Use the cryptocurrency/ohlcv/historical API call.')
        cryptocurrency_parser.add_argument('--price-performance-stats-latest', action='store_true',
                                           help='Use the cryptocurrency/price/performance/stats/latest API call.')

        exchange_parser = subparsers.add_parser(
            'exchange', help='Use the exchange endpoint.')
        exchange_parser.add_argument(
            '--map', action='store_true', help='Use the /v1/exchange/map API call.')
        exchange_parser.add_argument(
            '--info', action='store_true', help='Use the /v1/exchange/info API call.')
        exchange_parser.add_argument('--listings-latest', action='store_true',
                                     help='Use the /v1/exchange/listings/latest API call.')
        exchange_parser.add_argument('--listings-historical', action='store_true',
                                     help='Use the /v1/exchange/listings/historical API call.')
        exchange_parser.add_argument(
            '--quotes-latest', action='store_true', help='Use the /v1/exchange/quotes/latest API call.')
        exchange_parser.add_argument('--quotes-historical', action='store_true',
                                     help='Use the /v1/exchange/quotes/historical API call.')
        exchange_parser.add_argument('--market-pairs-latest', action='store_true',
                                     help='Use the /v1/exchange/market-pairs/latest API call.')

        global_metrics_parser = subparsers.add_parser(
            'global-metrics', help='Use the global-metrics endpoint.')
        global_metrics_parser.add_argument(
            '--latest', action='store_true', help='Use the /v1/global-metrics/quotes/latest API call.')
        global_metrics_parser.add_argument(
            '--historical', action='store_true', help='Use the /v1/global-metrics/quotes/historical API call.')

        tools_parser = subparsers.add_parser(
            'tools', help='Use the tools endpoint.')
        tools_parser.add_argument('--price-conversion', action='store_true',
                                  help='Use the /v1/tools/price-conversion API call.')

        blockchain_parser = subparsers.add_parser(
            'blockchain', help='Use the blockchain endpoint.')
        blockchain_parser.add_argument(
            '--latest', action='store_true', help='Use the /v1/blockchain/statistics/latest API call.')

        fiat_parser = subparsers.add_parser('fiat', help='Use the fiat endpoint.')
        fiat_parser.add_argument('--map', action='store_true',
                                 help='Use the /v1/fiat/map API call.')

        partners_parser = subparsers.add_parser(
            'partners', help='Use the partners endpoint.')
        partners_parser.add_argument('--listings-latest', action='store_true',
                                     help='Use the /v1/partners/flipside-crypto/fcas/listings/latest API call.')
        partners_parser.add_argument('--quotes-latest', action='store_true',
                                     help='Use the /v1/partners/flipside-crypto/fcas/quotes/latest API call.')

        key_parser = subparsers.add_parser('key', help='Use the key endpoint.')
        key_parser.add_argument('--info', action='store_true',
                                help='Use the /v1/key/info API call.')

        args = parser.parse_args()
        return args

    def user_requested_cryptocurrency_subparsers(self, args) -> list:
        """Subparsers for the cryptocurrency endpoint"""
        subparsers = []
        if args.map:
            subparsers.append('map')
        if args.info:
            subparsers.append('info')
        if args.listings_latest:
            subparsers.append('listings/latest')
        if args.listings_historical:
            subparsers.append('listings/historical')
        if args.quotes_latest:
            subparsers.append('quotes/latest')
        if args.quotes_historical:
            subparsers.append('quotes/historical')
        if args.market_pairs_latest:
            subparsers.append('market-pairs/latest')
        if args.ohlcv_latest:
            subparsers.append('ohlcv/latest')
        if args.ohlcv_historical:
            subparsers.append('ohlcv/historical')
        if args.price_performance_stats_latest:
            subparsers.append('price-performance-stats/latest')
        return subparsers

    def user_requested_exchange_subparsers(self, args) -> list:
        """Subparsers for the exchange endpoint"""
        subparsers = []
        if args.map:
            subparsers.append('map')
        if args.info:
            subparsers.append('info')
        if args.listings_latest:
            subparsers.append('listings/latest')
        if args.listings_historical:
            subparsers.append('listings/historical')
        if args.quotes_latest:
            subparsers.append('quotes/latest')
        if args.quotes_historical:
            subparsers.append('quotes/historical')
        if args.market_pairs_latest:
            subparsers.append('market-pairs/latest')
        return subparsers


    def user_requested_global_metrics_subparsers(self, args) -> list:
        """Subparsers for the global-metrics endpoint"""
        subparsers = []
        if args.latest:
            subparsers.append('latest')
        if args.historical:
            subparsers.append('historical')
        return subparsers


    def user_requested_tools_subparsers(self, args) -> list:
        """Subparsers for the tools endpoint"""
        subparsers = []
        if args.price_conversion:
            subparsers.append('price-conversion')
        return subparsers


    def user_requested_blockchain_subparsers(self, args) -> list:
        """Subparsers for the blockchain endpoint"""
        subparsers = []
        if args.latest:
            subparsers.append('latest')
        return subparsers


    def user_requested_fiat_subparsers(self, args) -> list:
        """Subparsers for the fiat endpoint"""
        subparsers = []
        if args.map:
            subparsers.append('map')
        return subparsers


    def user_requested_partners_subparsers(self, args) -> list:
        """Subparsers for the tools endpoint"""
        subparsers = []
        if args.listings_latest:
            subparsers.append('listings/latest')
        if args.quotes_latest:
            subparsers.append('quotes/latest')
        return subparsers


    def user_requested_key_subparsers(self, args) -> list:
        """Subparsers for the key endpoint"""
        subparsers = []
        if args.info:
            subparsers.append('info')
        return subparsers

    def command_parse(self, command) -> list:
        """Check the command parsed and grab subparsers"""
        if self.args.command == 'cryptocurrency':
            all_subparsers_requested = self.user_requested_cryptocurrency_subparsers(self.args)
        if self.args.command == 'exchange':
            all_subparsers_requested = self.user_requested_exchange_subparsers(self.args)
        if self.args.command == 'global-metrics':
            all_subparsers_requested = self.user_requested_global_metrics_subparsers(self.args)
        if self.args.command == 'tools':
            all_subparsers_requested = self.user_requested_tools_subparsers(self.args)
        if self.args.command == 'blockchain':
            all_subparsers_requested = self.user_requested_blockchain_subparsers(self.args)
        if self.args.command == 'fiat':
            all_subparsers_requested = self.user_requested_fiat_subparsers(self.args)
        if self.args.command == 'partners':
            all_subparsers_requested = self.user_requested_partners_subparsers(self.args)
        if self.args.command == 'key':
            all_subparsers_requested = self.user_requested_key_subparsers(self.args)
        return all_subparsers_requested


class APICall(object):
    """API calls to CoinMarketCap"""
    def __init__(self, your_api_key, list_of_urls):
        self.your_api_key = your_api_key
        self.list_of_urls = list_of_urls

    def api_key(self) -> str:
        """Return the api key."""
        return self.your_api_key

    def header(self) -> dict:
        """Custom header that must be set."""
        headers = {'Accepts': 'application/json',
                   'X-CMC_PRO_API_KEY': self.your_api_key
                   }
        return headers

    def parameters(self) -> dict:
        """Convert to USD, limit to 5000 entries."""
        parameters = {
                        'start':'1',
                        'limit':'5000',
                        'convert':'USD'
                    }
        return parameters

    def api_session(self, url) -> dict:
        """Make the API call"""
        session = requests.Session()
        session.headers.update(self.header())
        try:
            if 'info' in url or 'latest' in url:
                response = session.get(url, params=self.parameters())
            else:
                response = session.get(url)
            data = json.loads(response.text)
            return data
        except (requests.ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
            print(e)

    def loop_through_urls(self) -> list:
        """Loop through the URL's and make API calls, returning the API data in a list."""
        returned_data = []
        for url in self.list_of_urls:
            returned_data.append(self.api_session(url))
        # print(returned_data)
        return returned_data


class JSONParser(object):
    def __init__(self, api_dictionaries):
        self.status = 'status'
        self.data = 'data'
        self.statusCode = 'statusCode'
        self.api_dictionaries = api_dictionaries

    def print_status_table(self):
        """Status dictionary is short. Just print it."""
        for index in self.api_dictionaries:
            for key, value in index.items():
                if key == self.status:
                    if type(value) is dict:
                        # example: {'timestamp': '2020-04-11T05:54:24.228Z', 'error_code': 0, 'error_message': None, 'elapsed': 17, 'credit_count': 1}
                        headers = prettytable.PrettyTable(list(value.keys()))
                        headers.add_row(list(value.values()))
                        print(f'[*] {self.status}\n{headers}\n\n')

    def dictionary_parser(self, api_dictionaries, status_dictionary):
        """Input "status_dictionary" dictionary and dig through json layers to return lists."""
        table_headers = []
        table_content = []
        platform_keys = []
        platform_values = []
        quote_keys = []
        quote_values = []

        for index in api_dictionaries:
            for key, value in index.items():
                if key == status_dictionary:
                    if type(value) is dict:
                        # example: {'timestamp': '2020-04-11T05:54:24.228Z', 'error_code': 0, 'error_message': None, 'elapsed': 17, 'credit_count': 1}
                        headers = prettytable.PrettyTable(list(value.keys()))
                        headers.add_row(list(value.values()))
                        print(f'[*] {status_dictionary}\n{headers}\n\n')
                    if type(value) is list:
                        for index in value:
                            for key, value in index.items():
                                if type(value) is dict:
                                    if key == 'platform':
                                        platform_keys.append(list(value.keys()))
                                        platform_values.append(list(value.values()))
                                    # headers = prettytable.PrettyTable(platform_keys[0])
                                    # for index in platform_values:
                                    #     headers.add_row(index)
                                    if key == 'quote': # This will return {'USD': {'dict': 'value'}}. Need to fix this.
                                        quote_keys.append(list(value.keys()))
                                        quote_values.append(list(value.values()))
                            if index['platform']: # Don't return dict to list, just removed it.
                                del index['platform']
                            # if index.keys() == 'quote':
                            #     for key, value in value.items():
                            #         headers = prettytable.PrettyTable(list(index.keys()))
                            #         headers.add_row(list(value.values()))
                            #         print(f'[*] {key} for {list(index.values())[3]}\n{headers}\n\n')
                            if index['quote']: # Don't return dict to list, just removed it.
                                del index['quote']
                            table_headers.append(list(index.keys()))
                            table_content.append(list(index.values()))
                        # headers = prettytable.PrettyTable(table_headers[0])
                        # for index in table_content:
                        #     headers.add_row(index)
                        # print(f'[*] {status_dictionary}\n{headers}\n\n')
                        # print(table_content)
                    if type(value) is str:
                        print(f'I\'m a string that needs to be built!')
                        print(key)
                        # for keys, values in value.items():
                        #     print(keys)
                                # table_headers.append(keys)
                                # table_content.append(values)
                                # headers = prettytable.PrettyTable(table_headers)
                                # headers.add_row(table_content)
                                # print(f'[*] {status_dictionary}\n{headers}')
                                # table_headers = []
                                # table_content = []


    def print_dictionaries(self):
        """API call returned as is."""
        for index in self.api_dictionaries:
            print(index)