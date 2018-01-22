#!/usr/bin/env python
"""
    API client to pull cryptocurrency data from live exchange rates.

    Copyright (C) 2017  Mitch O'Donnell devreap1@gmail.com
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
import json
import pkg_resources
import urllib

import prettytable


class APICall(object):
    """
    API call is made and all coins extracted unless user passes coin.
    """

    def __init__(self, url, coins=None):
        self.url = url
        self.coins = coins or None
        self.response = urllib.urlopen(self.url)
        self.data = json.loads(self.response.read())

    def return_all_coins(self):
        """Make the API call and return all coin dictionaries."""
        return self.data

    def coins_with_value(self):
        """Filter coins with values into a dictionary."""
        coins_with_value = []
        for coin in self.coins[0]:
            if len(coin) > 1:
                temp_dict = {}
                temp_dict[coin[0]] = float(coin[1])
                coins_with_value.append(temp_dict)
        return coins_with_value

    def call_specified_coins(self, unique_coins):
        """Returns specified coin dictionaries requested by user."""
        dictionary_list = []
        for coin in unique_coins:
            for dictionary in self.data:
                if dictionary['id'] == coin:
                    dictionary_list.append(dictionary)
        return dictionary_list


def display_version():
    """Display the version of CoinMarketCap_API installed."""
    __version__ = pkg_resources.require('CoinMarketCap')[0].version
    print __version__


def display_license():
    """Display the micro license and point to the full license."""
    description = __doc__
    legal_statement = '\ncoinmarketcap_api.py Copyright (C) 2017  Mitch O\'Donnell\n\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.\n\nPlease read the full LICENSE file.\n'
    print description, legal_statement


def unique_coin_list(args_coins):
    """If user adds the same coin more than once, this function will filter it out."""
    unique_coin = []
    for lists in args_coins[0]:
        unique_coin.append(lists[0])
    unique_coin = list(set(unique_coin))
    return unique_coin


def decorate_coins(pull_coin_dictionary):
    """Format pull_coin_dictionary into ASCII tables."""
    headers = prettytable.PrettyTable(['id', 'name', 'symbol', 'rank', 'price_usd', 'price_btc', '24h_volume_usd', 'market_cap_usd',
                                       'available_supply', 'total_supply', 'max_supply ', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated'])
    for dictionary in pull_coin_dictionary:
        headers.add_row([dictionary['id'],
                         dictionary['name'],
                         dictionary['symbol'],
                         dictionary['rank'],
                         dictionary['price_usd'],
                         dictionary['price_btc'],
                         dictionary['24h_volume_usd'],
                         dictionary['market_cap_usd'],
                         dictionary['available_supply'],
                         dictionary['total_supply'],
                         dictionary['max_supply'],
                         dictionary['percent_change_1h'],
                         dictionary['percent_change_24h'],
                         dictionary['percent_change_7d'],
                         dictionary['last_updated']])
    print headers


def decorate_users_portfolio(coin_with_values, pull_coin_dictionary):
    """Import user coin portfolio and format to a table."""
    if not coin_with_values:
        return
    table = prettytable.PrettyTable(
        ['id', 'Coins in Wallet', 'Current Equity'])
    for dictionaries in pull_coin_dictionary:
        for coins in coin_with_values:
            for key, value in coins.iteritems():
                if dictionaries['id'] == key:
                    table.add_row(
                        [key, value, float(dictionaries['price_usd']) * float(value)])
    print '\n{}'.format(table)


def parse_arguments():
    """Capture user arguments to compile main()."""
    url = 'https://coinmarketcap.com/'
    api_address = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'
    epilog = '[*] Coin Exchange: {}\r\n[*] API Address: {}\r\n'.format(
        url, api_address)
    parser = argparse.ArgumentParser(
        epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    # parser.add_argument('-c', '--coins', nargs='*',
    #                     help='Add the coins you want to pull dictionaries.')
    parser.add_argument('-f', '--format', action='store_true',
                        help='Format dictionaries into a table.')
    parser.add_argument('-c', '--coins', action='append', type=lambda coin_value: coin_value.lower().split('='), nargs='*', dest='coins',
                        help='Provide coin names with/without the amount of coin in your wallet.\nExample: \n-c Bitcoin=10 eos ethereum=5\n-c bitcoin')
    parser.add_argument('-L', '--License', action='store_true', help='Print out the micro license for this software.\nSee LICENSE file for full license.')
    parser.add_argument('-V', '--Version', action='store_true', help='Print out the current version of coin_market installed.')
    parser.add_argument('-o', '--output', help='Send output to a file in .csv format.')
    args = parser.parse_args()
    return args


def main():
    """
    Pull the full list of coins in JSON format.
    If no arguments present, return all dictionaries.
    If arguments, return dictionaries with/without formatting.
    """

    args = parse_arguments()
    print args

    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'

    if args.coins:
        unique_coins = unique_coin_list(args.coins)
        request_coin_statistics = APICall(url, args.coins)
        pull_coin_dictionary = request_coin_statistics.call_specified_coins(
            unique_coins)
        coin_with_values = request_coin_statistics.coins_with_value()
        if args.format:
            decorate_coins(pull_coin_dictionary)
            decorate_users_portfolio(coin_with_values, pull_coin_dictionary)
        else:
            for dictionary in pull_coin_dictionary:
                print dictionary
            for dictionary in coin_with_values:
                print dictionary

    if args.License:
        display_license()

    if args.Version:
        display_version()

    if args.format and args.coins is None:
        request_coin_statistics = APICall(url)
        raw_coins_list = request_coin_statistics.return_all_coins()
        decorate_coins(raw_coins_list)

    # if args.coins is None and args.format is False:
    #     request_coin_statistics = APICall(url)
    #     raw_coins_list = request_coin_statistics.return_all_coins()
    #     for dictionary in raw_coins_list:
    #         print dictionary


if __name__ == '__main__':
    main()
