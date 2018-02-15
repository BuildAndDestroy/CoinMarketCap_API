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
import csv
import glob
import json
import urllib

import pkg_resources

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


def coin_portfolio_value(coin_with_values, pull_coin_dictionary):
    """
        Build lists of coin, your portfolio amount of coin, and USD amount.
        Return a list of lists.
    """
    coin_portfolio_value_list = []
    for dictionaries in pull_coin_dictionary:
        for coins in coin_with_values:
            for key, value in coins.iteritems():
                if dictionaries['id'] == key:
                    coin_portfolio_value_list.append(
                        [key, value, '{0:.3f}'.format(float(dictionaries['price_usd']) * float(value))])
    return coin_portfolio_value_list


def sort_dictionaries_alphabetically(pull_coin_dictionary):
    """Import the requested coin dictionaries and sort by name alphabetically."""
    sorted_dictionaries_by_name = sorted(pull_coin_dictionary, key=lambda x: x['name'])
    return sorted_dictionaries_by_name


def total_usd_amount(coin_portfolio_value_list):
    """Extract USD amount for each coin in portfolio, then add them together."""
    if not coin_portfolio_value_list:
        return

    usd_amount_list = []
    for lists in coin_portfolio_value_list:
        usd_amount_list.append(float(lists[2]))
    compile_usd_amount = reduce(
        lambda first_position, next_position: first_position + next_position, usd_amount_list)
    return '{0:.3f}'.format(float(compile_usd_amount))


def write_csv_file(coin_portfolio_value_list, total_portfolio_usd):
    """Create a csv file with portfolio data."""
    with open('portfolio.csv', 'w') as csv_file:
        fieldnames = ['id', 'Coins in Wallet', 'Current Equity']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fieldnames)
        for lists in coin_portfolio_value_list:
            csv_writer.writerow(lists)
        csv_writer.writerow(['Total Equity USD Amount'])
        csv_writer.writerow([total_portfolio_usd])


def read_csv_input():
    """Read csv file and return list of rows from the csv file."""
    portfolio_csv = glob.glob('portfolio.csv')
    list_to_decorate = []
    if not portfolio_csv:
        return 'No portfolio.csv file was found!'
    with open(portfolio_csv[0], 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list_to_decorate.append(row)
    return list_to_decorate


def decorate_coins(pull_coin_dictionary):
    """Format requested coins into a table."""
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


def decorate_users_portfolio(coin_portfolio_value_list):
    """Import user coin portfolio and format to a table."""
    if not coin_portfolio_value_list:
        return

    table = prettytable.PrettyTable(
        ['id', 'Coins in Wallet', 'Current Equity'])
    for lists in coin_portfolio_value_list:
        table.add_row(lists)
    print '\n{}'.format(table)


def decorate_portfolio_usd(total_portfolio_usd):
    """Decorate the USD portfolio amount."""
    if not total_portfolio_usd:
        return

    table = prettytable.PrettyTable(['Total Equity USD Amount'])
    table.add_row([total_portfolio_usd])
    print '\n{}'.format(table)


def decorate_imported_csv(read_portfolio_csv):
    """Decorate the imported csv file and print to terminal."""
    if read_portfolio_csv == 'No portfolio.csv file was found!':
        print read_portfolio_csv
        return

    coins_in_portfolio = []
    total_equity = []
    for lists in read_portfolio_csv:
        if len(lists) is 3:
            coins_in_portfolio.append(lists)
        else:
            total_equity.append(lists)

    portfolio_table = prettytable.PrettyTable(coins_in_portfolio[0])
    del coins_in_portfolio[0]
    for lists in coins_in_portfolio:
        portfolio_table.add_row(lists)

    equity_table = prettytable.PrettyTable(total_equity[0])
    del total_equity[0]
    for lists in total_equity:
        equity_table.add_row(lists)

    print '\n{}'.format(portfolio_table)
    print '\n{}'.format(equity_table)


def parse_arguments():
    """Capture user arguments to compile main()."""
    url = 'https://coinmarketcap.com/'
    api_address = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'
    epilog = '[*] Coin Exchange: {}\r\n[*] API Address: {}\r\n'.format(
        url, api_address)
    parser = argparse.ArgumentParser(
        epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
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
    args = parser.parse_args()
    return args


def main():
    """
    Pull the full list of coins in JSON format.
    If no arguments present, return all dictionaries.
    If arguments, return dictionaries with/without formatting.
    """

    args = parse_arguments()
    # print args

    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'

    if args.License:
        display_license()

    if args.Version:
        display_version()

    if args.coins:
        unique_coins = unique_coin_list(args.coins)
        request_coin_statistics = APICall(url, args.coins)
        pull_coin_dictionary = request_coin_statistics.call_specified_coins(
            unique_coins)

        if args.sort:
            pull_coin_dictionary = sort_dictionaries_alphabetically(pull_coin_dictionary)

        coin_with_values = request_coin_statistics.coins_with_value()
        coin_portfolio_value_list = coin_portfolio_value(
            coin_with_values, pull_coin_dictionary)
        total_portfolio_usd = total_usd_amount(coin_portfolio_value_list)

    if args.format and args.coins:
        decorate_coins(pull_coin_dictionary)
        decorate_users_portfolio(coin_portfolio_value_list)
        decorate_portfolio_usd(total_portfolio_usd)

    if args.coins is None and args.format is None:
        for dictionary in pull_coin_dictionary:
            print dictionary
        for dictionary in coin_with_values:
            print dictionary
        print total_portfolio_usd

    if args.output:
        write_csv_file(coin_portfolio_value_list, total_portfolio_usd)

    if args.format and args.coins is None and args.input is False:
        request_coin_statistics = APICall(url)
        raw_coins_list = request_coin_statistics.return_all_coins()
        decorate_coins(raw_coins_list)

    if args.coins is None and args.format is False and args.output is False and args.input is False and args.License is False and args.Version is False:
        request_coin_statistics = APICall(url)
        raw_coins_list = request_coin_statistics.return_all_coins()
        for dictionary in raw_coins_list:
            print dictionary

    if args.output and args.coins is None:
        print 'Must use with --coins.'

    if args.input:
        read_portfolio_csv = read_csv_input()
        if args.format:
            decorate_imported_csv(read_portfolio_csv)
        else:
            print read_portfolio_csv


if __name__ == '__main__':
    main()
