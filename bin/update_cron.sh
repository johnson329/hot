# crontab
# https://www.cnblogs.com/lowmanisbusy/p/12048054.html
#导出crontab 任务
sudo cat /var/spool/cron/crontabs/${USER} > crontabs.task
# 追加crontab任务
sudo cat mycron.task >> crontabs.task

sudo crontab -u ${USER} crontabs.task

