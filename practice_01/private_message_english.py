#! /usr/bin/env python
# -*- coding: utf8 -*-
# ----------------------------
# Name:         private_message_english
# Description:  
# Author:       WensentHuang
# Date:         2019-08-02
# ----------------------------

"""
加密表的规则:
第一行:abcdefghijklmnopqrstuvwxyz
第二行:nopqrstuvwxyzabcdefghijklm
当我们输入a的时候，加密后会变成n，b会变成o，以此类推
字符转十进制:ord('a')
十进制转字符:chr(97)
"""

message = input('Please input your message :')
# 声明一个变量, 接收加密后的字符串
result = ''
# 加密
for char in message:
    value = ord(char)
    print(('字符%s对应的ASCII码值:%s') % (char, value))
    if 64 < value < 78 or 96 < value < 110:
        result_char = chr(value + 13)
        result += result_char
    elif 77 < value < 91 or 109 < value < 123:
        result_char = chr(value - 13)
        result += result_char
    else:
        result += char

print('加密后的结果:', result)

# 解密
after_result = ''
for char in result:
    v = ord(char)
    if 64 < v < 78 or 96 < v < 110:
        result_char = chr(v + 13)
        after_result += result_char
    elif 77 < v < 91 or 109 < v < 123:
        result_char = chr(v - 13)
        after_result += result_char
    else:
        after_result += char

print('解密后的结果:', after_result)


