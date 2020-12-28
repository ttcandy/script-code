#!/usr/local/python3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   手机号码随机生成重构.py    
@Contact :   tt_candy@outlook.com
@License :   仅供非生产环境使用
@Desciption: 随机生成手机号码，号码仅用于数据分析测试
@Creation time：20/12/28 9:07

@Modify Time      @Author    @Version    @Modify action
------------      -------    --------    -----------
   None           ttcandy      2.0         None
'''
from multiprocessing import Process
from random import choice,randint
import gevent
from datetime import datetime
'''
主体：
1.生成手机号码头部--运营商以手机号前3-4位区分
2.生成手机号尾部
3.生成手机号码
4.写入文件
5.使用多进程和协程并发写入文件
'''

class Phone():

    ph_them_roughly = {
        "中国电信": ['133', '149', '153', '173', '177', '180', '181', '189', '190', '191', '193', '199'],
        "中国联通": ['130', '131', '132', '145', '146', '155', '156', '166', '171', '175', '176', '185', '186', '196'],
        "中国移动": [['134', list(range(0, 9))], '135', '136', '137', '138', '139', '147', '148', '150', '151', '152',
                 '157', '158', '159', '172', '178', '182', '183', '184', '187', '188', '195', '197', '198'],
        "中国广电": ['192'],
        "网卡专属": ['145', '147'],
        "物联网业务": ['146', '148'],
        "卫星通信": '1349',
        "虚拟运营商-电信": ['1700', '1701', '1702', '162'],
        "虚拟运营商-移动": ['1703', '1705', '1706', '165'],
        "虚拟运营商-联通": ['1704', '1707', '1708', '1709', '167', '171']
    }
    ph_manufacturer_list = ["中国电信", "中国联通", "中国移动"]
    '''
    ph_them_roughly：手机号码头部匹配字典(tpye：tulpe,keys:ph_manufacturer_list中元素，value:list)
    ph_manufacturer_list：需求生成的手机号码运营商(tpye:元素必须是ph_them_roughly[keys]存在的str)
    '''

    def ph_head(self):
        '''
        随机列表ph_manufacturer_list，获取运营商，返回运营商和对应号码头部列表
        :return:ph_manu
        '''
        ph_manu=choice(self.ph_manufacturer_list)       #随机获取ph_manufacturer_list列表运营商
        ph_manu=[ph_manu]       #转义为列表使其成为定值
        ph_head_num=choice(self.ph_them_roughly[ph_manu[0]])       #随机获取ph_them_roughly value列表中元素
        if isinstance(ph_head_num,str):     #判断获取的元素是否是字符串
            ph_manu.append(ph_head_num)     #添加到手机号码头部至列表
            return ph_manu
        else:
            ph_head_num=ph_head_num[0]+str(choice(ph_head_num[1]))      #随机获取ph_head_num[1]元素，拼接字符串
            ph_manu.append(ph_head_num)
            return ph_manu

    def ph_tail(self):
        '''
        生成八位随机数字字符串
        :return:ph_tail_num
        '''
        ph_tail_num=""      #定义一个空的字符串
        while len(ph_tail_num) < 8 :        #判断生成的ph_tail_num长度，从0开始到7，共八位
            ph_tail_num=ph_tail_num + str(randint(0,9))        #随机获取num_list元素
        return ph_tail_num

    @staticmethod
    def ph_num():
        '''
        拼接手机号码，返回完整运营商和手机号码列表
        :return:ph_list
        '''
        ph=Phone()      #赋值Phone类对象
        ph_list=ph.ph_head()        #实例化ph_head类方法
        if len(ph_list[1]) == 3:        #判断号码头部长度
            ph_list[1] = ph_list[1] + ph.ph_tail()      #拼接手机号码，并重新赋值ph_list[1]
            return ph_list
        else:
            ph_list[1] = ph_list[1] + ph.ph_tail()[:7]      #保留7位尾部，拼接手机号码，重新赋值ph_list[1]
            return ph_list


if __name__=="__main__":

    filename="上门服务.txt"
    nums = 10000000
    with open(filename, "a", encoding="UTF-8") as f:
        while nums > 0:
            ph=Phone.ph_num()
            f.write(ph[0]+","+ph[1]+"\n")
            nums -=1