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


# 回溯法找到某个key的路径
def get_hots():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        "Cookie": ""}
    zh_url = "https://www.zhihu.com/billboard"
    zh_response = requests.get(zh_url, headers=headers)

    zh_response.encoding = 'utf-8'
    content = zh_response.text
    html = etree.HTML(content)
    json_data = html.xpath('//script[@id="js-initialData"]/text()')
    json_data[0] = json.loads(str(json_data[0]))

    hot_list = json_data[0].get('initialState').get('topstory').get('hotList')

    for index, i in enumerate(hot_list):
        index += 1
        title = i.get('target').get('titleArea').get('text')
        link = i.get('target').get('link').get('url')
        hot = i.get('target').get('metricsArea').get('text')
        category = 'zhihu'
        data = {
            'title': title,
            'hot': hot,
            'link': link,
            'category': category,
            'time':arrow.now().format("YYYY-MM-DD HH:mm")
        }
        mycol.insert_one(data)
    print('获取热搜成功{}'.format(arrow.now().format("YYYY-MM-DD HH:mm:ss ZZ")))

    # data = []
    # for li in result:
    #     try:
    #         num = li.xpath('./div[1]/div[1]/text()')[0]
    #         title = li.xpath('./div[2]/div[1]/text()')[0]
    #         hot = li.xpath('./div[2]/div[2]/text()')[0]
    #         data.append([num, title, hot, ])
    #     except Exception as e:
    #         # 异常保存，第二天，分析，单独爬取。
    #         print(e)


if __name__ == '__main__':
    get_hots()
