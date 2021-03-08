#!/bin/bash
# docker with docker-compose
docker -v
if [ $? -eq  0 ]; then
  echo "检查到Docker已安装!"
else
  echo "安装docker环境..."
  curl -sSL https://get.daocloud.io/docker | sh
  curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
  echo "安装docker环境...安装完成!"
fi

# clone project
cd $HOME/hot
docker-compose up -d
sudo apt install virtualenv
virtualenv --python=python3 env
$HOME/hot/env/bin/pip3 install -r requirements.txt -i http://pypi.douban.com/simple/