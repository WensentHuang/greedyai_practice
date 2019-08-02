#! /usr/bin/env python
# -*- coding: utf8 -*-
# ----------------------------
# Name:         private_message_chinese
# Description:  
# Author:       WensentHuang
# Date:         2019-08-02
# ----------------------------

import requests
import re

# 爬取汉字信息
html_result = requests.get('https://www.zdic.net/zd/zb/cc1')
reg = "/hans/(.*)' "
hans_list = re.findall(reg, html_result.text)

print(hans_list)

message = input('please input your message: ')
result = ''

# 加密
for i in message:
    for index, han in enumerate(hans_list):
        if i == han:
            result += str(index) + '|'

print('加密后的字符串: ', result)

# 解密
after_result = ''
index_list = result.split('|')
index_list.remove('')
for index in index_list:
    after_result += hans_list[int(index)]

print('解密后的字符串: ', after_result)