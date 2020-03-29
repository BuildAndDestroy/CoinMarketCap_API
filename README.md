
## NEW BUILD REQUIRED

The API server is now dead. We are met with:

```
{"statusCode": 410,"error": "Gone","message": "WARNING: This API is now offline. Please switch to the new CoinMarketCap API. (https://pro.coinmarketcap.com/migrate/)"}
```
* Rebuild with python3
* Convert to the new API


## Dockerfile install
```
docker build -t buildanddestroy/coin_market_cap .
docker run --rm -it buildanddestroy/coin_market_cap /bin/bash
```

## Pull image from Dockerhub
```
docker pull buildanddestroy/coin_market_cap
```

## Install into the OS 

```
sudo pip install .
```

* If upgrading, run:
```
sudo pip install --upgrade .
```

## Install into a virtual environment
```
virtualenv coin_cap
source coin_cap/bin/activate
pip install /path/to/CoinMarketCap_API/.
```

###### Help Menu:
```
usage: coin_market.py [-h] [-c [COINS [COINS ...]]] [-f]

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

optional arguments:
  -h, --help            show this help message and exit
  -c [COINS [COINS ...]], --coins [COINS [COINS ...]]
                        Add the coins you want to pull dictionaries.
  -f, --format          Format dictionaries into a table

[*] Coin Exchange: https://coinmarketcap.com/
[*] API Address: https://api.coinmarketcap.com/v1/ticker/?limit=0

coin_market.py Copyright (C) 2017  Mitch O'Donnell
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
```



###### Examples:

* Formatting with called out coins (make terminal text small to read table):
```
 ~ $ coin_market -c bitcoin bitcoin-cash bitcoin-gold ethereum litecoin dash eos monero dogecoin -f


+--------------+--------------+--------+------+------------+------------+----------------+----------------+------------------+--------------+-------------+-------------------+--------------------+-------------------+--------------+
|      id      |     name     | symbol | rank | price_usd  | price_btc  | 24h_volume_usd | market_cap_usd | available_supply | total_supply | max_supply  | percent_change_1h | percent_change_24h | percent_change_7d | last_updated |
+--------------+--------------+--------+------+------------+------------+----------------+----------------+------------------+--------------+-------------+-------------------+--------------------+-------------------+--------------+
|   bitcoin    |   Bitcoin    |  BTC   |  1   |  8268.42   |    1.0     |  4818860000.0  |  138080960316  |    16699800.0    |  16699800.0  |  21000000.0 |        0.42       |        2.26        |        7.72       |  1511586850  |
| bitcoin-cash | Bitcoin Cash |  BCH   |  3   |  1598.11   |  0.19367   |  2492640000.0  | 26881588570.0  |    16820863.0    |  16820863.0  |  21000000.0 |        0.1        |       -4.77        |       25.71       |  1511586867  |
| bitcoin-gold | Bitcoin Gold |  BTG   | 1028 |  384.931   | 0.0466487  |  506422000.0   |      None      |       None       |  16765449.0  |  21000000.0 |        0.64       |       13.81        |       136.16      |  1511586874  |
|   ethereum   |   Ethereum   |  ETH   |  2   |  475.275   | 0.0575972  |  2456650000.0  | 45596948485.0  |    95938033.0    |  95938033.0  |     None    |        1.75       |       15.21        |       43.69       |  1511586852  |
|   litecoin   |   Litecoin   |  LTC   |  6   |  79.3272   | 0.00961343 |  315424000.0   |  4281991676.0  |    53978858.0    |  53978858.0  |  84000000.0 |        0.82       |        7.34        |       18.39       |  1511586842  |
|     dash     |     Dash     |  DASH  |  5   |  595.352   |  0.072149  |  172073000.0   |  4589535818.0  |    7708945.0     |  7708945.0   |  18900000.0 |        2.52       |        5.32        |       33.94       |  1511586846  |
|     eos      |     EOS      |  EOS   |  15  |  1.82312   | 0.00022094 |   42032300.0   |  908545916.0   |   498346744.0    | 1000000000.0 |     None    |        1.3        |        2.1         |        3.66       |  1511586866  |
|    monero    |    Monero    |  XMR   |  7   |  162.529   | 0.0196964  |   74228300.0   |  2502342237.0  |    15396282.0    |  15396282.0  |     None    |        0.72       |        1.97        |       29.41       |  1511586844  |
|   dogecoin   |   Dogecoin   |  DOGE  |  35  | 0.00193866 | 0.00000023 |   9087690.0    |  217248776.0   |   112061308384   | 112061308384 |     None    |        0.81       |        1.62        |       49.14       |  1511586843  |
+--------------+--------------+--------+------+------------+------------+----------------+----------------+------------------+--------------+-------------+-------------------+--------------------+-------------------+--------------+
```


* Without formatting, leaving the JSON output for end user use.:
```
 ~ $ coin_market -c bitcoin bitcoin-cash bitcoin-gold ethereum litecoin dash eos monero dogecoin

{u'market_cap_usd': u'138080960316', u'price_usd': u'8268.42', u'last_updated': u'1511586850', u'name': u'Bitcoin', u'24h_volume_usd': u'4818860000.0', u'percent_change_7d': u'7.72', u'symbol': u'BTC', u'max_supply': u'21000000.0', u'rank': u'1', u'percent_change_1h': u'0.42', u'total_supply': u'16699800.0', u'price_btc': u'1.0', u'available_supply': u'16699800.0', u'percent_change_24h': u'2.26', u'id': u'bitcoin'}
{u'market_cap_usd': u'26881588570.0', u'price_usd': u'1598.11', u'last_updated': u'1511586867', u'name': u'Bitcoin Cash', u'24h_volume_usd': u'2492640000.0', u'percent_change_7d': u'25.71', u'symbol': u'BCH', u'max_supply': u'21000000.0', u'rank': u'3', u'percent_change_1h': u'0.1', u'total_supply': u'16820863.0', u'price_btc': u'0.19367', u'available_supply': u'16820863.0', u'percent_change_24h': u'-4.77', u'id': u'bitcoin-cash'}
{u'market_cap_usd': None, u'price_usd': u'384.931', u'last_updated': u'1511586874', u'name': u'Bitcoin Gold', u'24h_volume_usd': u'506422000.0', u'percent_change_7d': u'136.16', u'symbol': u'BTG', u'max_supply': u'21000000.0', u'rank': u'1028', u'percent_change_1h': u'0.64', u'total_supply': u'16765449.0', u'price_btc': u'0.0466487', u'available_supply': None, u'percent_change_24h': u'13.81', u'id': u'bitcoin-gold'}
{u'market_cap_usd': u'45596948485.0', u'price_usd': u'475.275', u'last_updated': u'1511586852', u'name': u'Ethereum', u'24h_volume_usd': u'2456650000.0', u'percent_change_7d': u'43.69', u'symbol': u'ETH', u'max_supply': None, u'rank': u'2', u'percent_change_1h': u'1.75', u'total_supply': u'95938033.0', u'price_btc': u'0.0575972', u'available_supply': u'95938033.0', u'percent_change_24h': u'15.21', u'id': u'ethereum'}
{u'market_cap_usd': u'4281991676.0', u'price_usd': u'79.3272', u'last_updated': u'1511586842', u'name': u'Litecoin', u'24h_volume_usd': u'315424000.0', u'percent_change_7d': u'18.39', u'symbol': u'LTC', u'max_supply': u'84000000.0', u'rank': u'6', u'percent_change_1h': u'0.82', u'total_supply': u'53978858.0', u'price_btc': u'0.00961343', u'available_supply': u'53978858.0', u'percent_change_24h': u'7.34', u'id': u'litecoin'}
{u'market_cap_usd': u'4589535818.0', u'price_usd': u'595.352', u'last_updated': u'1511586846', u'name': u'Dash', u'24h_volume_usd': u'172073000.0', u'percent_change_7d': u'33.94', u'symbol': u'DASH', u'max_supply': u'18900000.0', u'rank': u'5', u'percent_change_1h': u'2.52', u'total_supply': u'7708945.0', u'price_btc': u'0.072149', u'available_supply': u'7708945.0', u'percent_change_24h': u'5.32', u'id': u'dash'}
{u'market_cap_usd': u'908545916.0', u'price_usd': u'1.82312', u'last_updated': u'1511586866', u'name': u'EOS', u'24h_volume_usd': u'42032300.0', u'percent_change_7d': u'3.66', u'symbol': u'EOS', u'max_supply': None, u'rank': u'15', u'percent_change_1h': u'1.3', u'total_supply': u'1000000000.0', u'price_btc': u'0.00022094', u'available_supply': u'498346744.0', u'percent_change_24h': u'2.1', u'id': u'eos'}
{u'market_cap_usd': u'2502342237.0', u'price_usd': u'162.529', u'last_updated': u'1511586844', u'name': u'Monero', u'24h_volume_usd': u'74228300.0', u'percent_change_7d': u'29.41', u'symbol': u'XMR', u'max_supply': None, u'rank': u'7', u'percent_change_1h': u'0.72', u'total_supply': u'15396282.0', u'price_btc': u'0.0196964', u'available_supply': u'15396282.0', u'percent_change_24h': u'1.97', u'id': u'monero'}
{u'market_cap_usd': u'217248776.0', u'price_usd': u'0.00193866', u'last_updated': u'1511586843', u'name': u'Dogecoin', u'24h_volume_usd': u'9087690.0', u'percent_change_7d': u'49.14', u'symbol': u'DOGE', u'max_supply': None, u'rank': u'35', u'percent_change_1h': u'0.81', u'total_supply': u'112061308384', u'price_btc': u'0.00000023', u'available_supply': u'112061308384', u'percent_change_24h': u'1.62', u'id': u'dogecoin'}
```
