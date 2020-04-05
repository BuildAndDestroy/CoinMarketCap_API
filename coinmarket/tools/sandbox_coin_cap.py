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

from coinmarket.lib import about_this_app


def parse_arguments() -> tuple:
    """Give options for user input."""
    url = 'https://sandbox-api.coinmarketcap.com/'
    epilog = f'[*] Tool used for sandbox working with the sandbox environment.\n[*] {url}'
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


def main() -> None:
    """Pull the full list of coins in JSON format.

    If no arguments present, return all dictionaries.
    If arguments, return dictionaries with/without formatting.
    """
    print(f'[*] ****Coming soon!****\n')

    args = parse_arguments()
    print(args)
    if args.License:
        about_this_app.display_license()
    if args.Version:
        about_this_app.display_version()

    # move all this into their own functions/methods
    subparsers = []
    if args.command == 'cryptocurrency':
        print('We hit crypto!')
        #api = CoinMarketCapURL(args.your_api_key, )
        if args.map:
            print('Map hit!')
            subparsers.append(args.map)
        if args.info:
            print('Info hit!')
            # subparsers.append()
        if args.listings_latest:
            print('listings_latest hit!')
            # subparsers.append()
        if args.listings_historical:
            print('listings_historical hit!')
            # subparsers.append()
        if args.quotes_latest:
            print('quotes_latest hit!')
            # subparsers.append()
        if args.quotes_historical:
            print('quotes_historical hit!')
            # subparsers.append()
        if args.market_pairs_latest:
            print('market_pairs_latest hit!')
            # subparsers.append()
        if args.ohlcv_latest:
            print('ohlcv_latest hit!')
            # subparsers.append()
        if args.ohlcv_historical:
            print('ohlcv_historical hit!')
            # subparsers.append('ohlcv/historical')
        if args.price_performance_stats_latest:
            print('price_performance_stats_latest hit!')
            # subparsers.append()

    if args.command == 'exchange':
        print('We hit exchange!')
        if args.map:
            print('We hit map')
        if args.info:
            print('We hit info')
        if args.listings_latest:
            print('We hit listings_latest')
        if args.listings_historical:
            print('We hit listings_historical')
        if args.quotes_latest:
            print('We hit quotes_latest')
        if args.quotes_historical:
            print('We hit quotes_historical')
        if args.market_pairs_latest:
            print('We hit market_pairs_latest')

    if args.command == 'global-metrics':
        print('We hit global-metrics!')
        if args.latest:
            print('We hit latest')
        if args.historical:
            print('We hit historical')

    if args.command == 'tools':
        print('We hit tools!')
        if args.price_conversion:
            print('We hit price_conversion')

    if args.command == 'blockchain':
        print('We hit blockchain!')
        if args.latest:
            print('We hit latest')

    if args.command == 'fiat':
        print('We hit fiat!')
        if args.map:
            print('We hit map')

    if args.command == 'partners':
        print('We hit partners!')
        if args.listings_latest:
            print('We hit listings_latest')
        if args.quotes_latest:
            print('We hit quotes_latest')

    if args.command == 'key':
        print('We hit key!')
        if args.info:
            print('We hit info')


if __name__ == '__main__':
    main()
