
Required modules, will be installed on pip install:

argparse
json
prettytable
urllib

Install this program into the system (tested on Linux), clone or download zip. Change directory until setup.py is in the same directory, then run:

sudo pip install .


If upgrading, run:

sudo pip install --upgrade .


Help Menu:

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
