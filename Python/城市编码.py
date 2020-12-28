#!/usr/bin/
# -*- encoding: utf-8 -*-
'''
@File    :   手机号码随机生成.py
@Contact :   tt_candy@outlook.com
@License :   仅供非生产环境使用
@Desciption: 爬取国内城市编码
@Creation time：20/12/21 9:42

@Modify Time      @Author    @Version    @Modify action
------------      -------    --------    -----------
   None           ttcandy      1.0         None
'''

import requests
from lxml import etree

url = "http://hotel.alitrip.com/area.htm?tbpm=3&domestic=0&enName=&page=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

response = requests.get(url=url,headers=headers)
page_city_name = response.content.decode('GBK')

tree = etree.HTML(page_city_name)
tr_list = tree.xpath('/html/body/div/table/tbody/tr')
with open('city_name.txt','w',encoding='utf-8') as fp:
    for td in tr_list:
        city_name = td.xpath('./td//text()')
        #len_city_name = len(city_name)
        fp.write(city_name[0]+','+city_name[1]+'\n')
        print(city_name[1]+'~~载入成功')
