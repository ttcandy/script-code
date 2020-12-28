#!/usr/bin/
# -*- encoding: utf-8 -*-
'''
@File    :   with_备份文件.py
@Contact :   tt_candy@outlook.com
@License :   请谨慎阅读下面的功能说明，以免产生不可逆因素
@Desciption: 文件修改并备份
@Creation time：20/12/21 10:43

@Modify Time      @Author    @Version    @Modify action
------------      -------    --------    -----------
   None           ttcandy      1.0         None
'''

import os

file_original="text.txt"        #备份文件名称
file_modify="t.txt"     #备份后文件临时名称
file_encoding="UTF-8"       #指定编码
ord_change="ds"
new_change="你麻痹"


with open(file_original,"r",encoding=file_encoding) as fo,\
        open(file_modify,"w",encoding=file_encoding) as fm:
    for i in fo:
        i = i.replace(ord_change,new_change)       #更换原文件内容
        fm.write(i)

file_original_bak="{}.bak".format(file_original)
if os.path.exists(file_original_bak) ==True:
    os.remove(file_original_bak)        #判断bak文件存在删除
    os.rename(file_original, file_original_bak)     #备份原文件
else:
    os.rename(file_original,file_original_bak)
print("{}文件已更新".format(file_original))

os.rename(file_modify,file_original)        #修改后文件重命名
print('{}文件已备份'.format(file_original_bak))