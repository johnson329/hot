# clone project
cd $HOME/hot
docker-compose up -d
sudo apt install virtualenv
ls $HOME/hot
if [ $? -eq  0 ]; then
  git pull
  echo "项目存在"
else
  virtualenv --python=python3 env
fi
$HOME/hot/env/bin/pip3 install -r requirements.txt -i http://pypi.douban.com/simple/
