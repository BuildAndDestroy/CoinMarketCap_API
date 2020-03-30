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


class CoinMarketCapURL(object):
    """URL build sessions for the api call to the Sandbox environment."""

    def __init__(self, your_api_key):
        self.sandbox_base_url = 'https://sandbox-api.coinmarketcap.com/v1'
        self.prod_base_url = 'https://pro-api.coinmarketcap.com/v1'
        self.your_api_key = your_api_key
        self.header = self.header()

    def api_key(self) -> str:
        """Return the api key."""
        return self.your_api_key

    def header(self) -> dict:
        """Custom header that must be set."""
        headers = {'Accepts': 'application/json',
                   'X-CMC_PRO_API_KEY': self.your_api_key
                   }
        return headers

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

    def generate_url(self, endpoint) -> str:
        """"""
        endpoint_dictionary = self.endpoint_dictionary()

        # This is a generator to check all possible URL's to call.
        for key, value in endpoint_dictionary.items():
            for index in value:
                print(f'{self.sandbox_base_url}{key}{index}')

    def get_sandbox_api_key(self) -> str:
        """If no API key is set, tell user where to get one."""
        url = 'https://sandbox.coinmarketcap.com/'
        return f'[*] No API Key is set.\n    Get your Sandbox API key at {url}'

    def get_prod_api_key(self) -> str:
        """If no API key is set, tell user where to get one."""
        url = 'https://pro.coinmarketcap.com/'
        return f'[*] No API Key is set.\n    Get your Production API key at {url}'

