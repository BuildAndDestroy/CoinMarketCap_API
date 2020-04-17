## New CoinMarketCap Build!
More to come, still beta but calls are starting to work for the sandbox environment


## Dockerfile install
```
docker build -t yourusername/coin_market_cap .
docker run --rm -it yourusername/coin_market_cap /bin/bash
```

## Pull image from Dockerhub
```
docker pull buildanddestroy/coin_market_cap
```

## Install into the OS 

```
sudo pip3 install .
```

* If upgrading, run:
```
sudo pip3 install --upgrade .
```

## Install into a virtual environment
```
virtualenv -p python3 coin_cap
source coin_cap/bin/activate
pip install /path/to/CoinMarketCap_API/.
```
