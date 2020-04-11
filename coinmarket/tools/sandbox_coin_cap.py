#!/usr/bin/env python3
"""API client to pull cryptocurrency data from the CoinMarketCap Sandbox.

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
ENVIRONMENT = 'sandbox'

from coinmarket.lib import about_this_app
from coinmarket.lib import coin_api


def main() -> None:
    """Pull the full list of coins in JSON format.

    Arguments needed, return dictionaries with/without formatting.
    """
    user_input = coin_api.UserArguments(ENVIRONMENT)
    if user_input.args.License:
        about_this_app.display_license()
    if user_input.args.Version:
        about_this_app.display_version()

    if user_input.args.command:
        subparsers = user_input.command_parse(user_input.args.command)
        api = coin_api.CoinMarketCapURL(ENVIRONMENT)
        all_api_urls = api.generate_urls(user_input.args.command, subparsers)
        initiate_api = coin_api.APICall(user_input.args.your_api_key, all_api_urls)
        api_dictionaries = initiate_api.loop_through_urls()
        #status_dictionaries = coin_api.separate_dictionaries(api_dictionaries, 'status')
        # data_dictionaries = separate_dictionaries(api_dictionaries, 'data')
        if user_input.args.format:
            coin_api.format_status_dictionary(api_dictionaries, 'status')
            coin_api.format_status_dictionary(api_dictionaries, 'data')
            coin_api.format_status_dictionary(api_dictionaries, 'statusCode')
        if not user_input.args.format:
            coin_api.print_dictionaries(api_dictionaries)

if __name__ == '__main__':
    main()
