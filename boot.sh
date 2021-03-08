#!/bin/bash
# docker with docker-compose
curl -sSL https://get.daocloud.io/docker | sh
curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# clone project
cd $HOME/hot
docker-compose up -d
sudo apt install virtualenv
virtualenv --python=python3 env
$HOME/hot/env/bin/pip3 install -r requirements -i http://pypi.douban.com/simple/

# crontab
# https://www.cnblogs.com/lowmanisbusy/p/12048054.html
#导出crontab 任务
sudo cat /var/spool/cron/crontabs/${USER} > crontabs.task
# 追加crontab任务
sudo cat mycron.task >> crontabs.task

sudo crontab -u ${USER} crontabs.task

