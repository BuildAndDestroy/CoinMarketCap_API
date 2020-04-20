FROM ubuntu:bionic
RUN apt update -y
RUN apt install software-properties-common -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 --version; pip3 install --upgrade pip
RUN mkdir /opt/coin_market_cap/
COPY ./ /opt/coin_market_cap/
RUN useradd -ms /bin/bash coin-user
USER coin-user
ENV PATH=$PATH:/home/coin-user/.local/bin
RUN pip3 install /opt/coin_market_cap/.
