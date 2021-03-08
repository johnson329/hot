# clone project
cd $HOME/hot
docker-compose up -d
sudo apt install virtualenv
virtualenv --python=python3 env
$HOME/hot/env/bin/pip3 install -r requirements.txt -i http://pypi.douban.com/simple/