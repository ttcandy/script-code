#!/usr/bin/
# -*- encoding: utf-8 -*-
'''
@File    :   手机号码随机生成1.0.py
@Contact :   tt_candy@outlook.com
@License :   仅供非生产环境使用
@Desciption: 随机生成手机号码，号码仅用于数据分析测试
@Creation time：20/12/21 9:42

@Modify Time      @Author    @Version    @Modify action
------------      -------    --------    -----------
   None           ttcandy      1.0         None  
'''
import random
import time

phone_them_roughly={
    "中国电信":[ '133','149','153','173','177','180','181','189','190','191','193','199' ],
    "中国联通":[ '130','131','132','145','146','155','156','166','171','175','176','185','186','196' ],
    "中国移动":[ ['134',list(range(0,9))],'135','136','137','138','139','147','148','150','151','152','157','158','159','172','178','182','183','184','187','188','195','197','198' ],
    "中国广电":[ '192' ],
    "网卡专属":[ '145','147' ],
    "物联网业务":[ '146','148' ],
    "卫星通信":'1349',
    "虚拟运营商-电信":[ '1700','1701','1702','162' ],
    "虚拟运营商-移动":[ '1703','1705','1706' ,'165' ],
    "虚拟运营商-联通":[ '1704','1707','1708','1709','167','171' ],
}
phone_manufacturer_list=["中国电信","中国联通","中国移动"]       #手机号运营商
phone_nums=10000              #手机号数量
filename='上门服务.txt'     #生成文件名

def Phone_head():
    """
    随机生成手机号码头部
    :return: phone_head
    """
    phone_manufacturer=phone_manufacturer_list[random.randint(0, len(phone_manufacturer_list)-1)]       #len获取营运商列表长度，生成0到len(phone_manufacturer_list)-1的运营商列表索引长度，随机得到运营商名称
    phone_head_list=phone_them_roughly[phone_manufacturer]        #调用Phone_manufacturer()函数,得到对应运营商手机号段列表
    phone_head=phone_head_list[random.randint(0,len(phone_head_list)-1)]        #取得运营商手机号段列表长度,随机得到索引，得到手机号码头部
    if isinstance(phone_head,str):      #判断手机号码头部为字符串
        return  phone_head
    else:
        return phone_head[0]+str(phone_head[1][random.randint(0, len(phone_head[1]) - 1)])  # “134“号段比其他多一位，特殊处理

def Phone_num():
    '''
    生成手机号码
    :return: phone_num
    '''
    phone_num=Phone_head()
    phone_long=len(phone_num)     #调用Phone_head(),获得手机号临时长度
    while phone_long < 11 :
        phone_num=phone_num + str(random.randint(0,9))      #叠加生成11位手机号码
        phone_long=len(phone_num)
    return phone_num

def Manufacturer(phone):
    '''
    判断手机号码运营商
    :return: key
    '''
    phone=str(phone)
    for key in phone_them_roughly:
        for head in phone_them_roughly[key]:
            if phone == head:
                return key
            else:
                for i in head:
                    if phone == i:
                        return  key

with open(filename,'a',encoding='UTF-8') as f:
    while phone_nums > 0 :
        phone_num=Phone_num()
        phone_manufacturer=Manufacturer(phone_num[0:3])
        phone_nums -=1
        phone="{}：{}".format(phone_manufacturer,phone_num)
        print("{} 已写入文件".format(phone))
        f.write(phone+"\n")
        #time.sleep(1)