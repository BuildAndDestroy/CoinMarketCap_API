FROM ubuntu:bionic
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python-pip -y
RUN pip --version; pip install --upgrade pip
RUN mkdir /opt/coin_market__cap/
COPY ./ /opt/coin_market_cap/
RUN pip install /opt/coin_market_cap/.
