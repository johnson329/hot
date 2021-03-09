import requests
import json

import arrow
from loguru import logger
import pymongo
import requests
from lxml import etree


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.admin
mydb.authenticate("admin", "123.com")
mydb = myclient["hot"]

mycol = mydb["hot"]
# cookies = {
#     'BAIDUID': '2D9DCDC9DBBB4EEE8706317E2297A464:FG=1',
#     'Hm_lvt_79a0e9c520104773e13ccd072bc956aa': '1615300196',
#     'bdshare_firstime': '1615300196421',
#     'Hm_lpvt_79a0e9c520104773e13ccd072bc956aa': '1615300293',
# }
def get_baidu_hots():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh',
    }

    params = (
        ('b', '1'),
        ('fr', 'topindex'),
    )

    response = requests.get('https://top.baidu.com/buzz', headers=headers, params=params)
    response.encoding = 'gb2312'
    xpath_clause = '//table[@class="list-table"]/tr'
    html = etree.HTML(response.text)
    items = html.xpath(xpath_clause)
    for item in items:
        if item.xpath('./td[@class="keyword"]'):
            link = item.xpath('./td[@class="keyword"]/a[1]/@href')[0]
            title = item.xpath('./td[@class="keyword"]/a[1]/text()')[0]
            hot = item.xpath('./td[@class="last"]/span/text()')[0]

            category = 'baidu'
            data = {
                'title': title,
                'hot': hot,
                'link': link,
                'category': category,
                'time': arrow.now().format("YYYY-MM-DD HH:mm")
            }
            mycol.insert_one(data)
            # print(title)
            # print(data)

            print('获取热搜成功{}'.format(arrow.now().format("YYYY-MM-DD HH:mm:ss ZZ")))


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://top.baidu.com/buzz?b=1&fr=topindex', headers=headers, cookies=cookies)
if __name__ == '__main__':
    get_baidu_hots()
