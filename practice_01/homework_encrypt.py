#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -------------------------------
# Name:          homework_encrypt
# Description:
# Author:        WensentHuang
# Date:          2019-08-04
# -------------------------------

import requests
import re

"""
自己写一个加密程序，能够加密英文和汉字， 同时加密并且解密
加密规则： 获取ascii码数字， 中间用|分割
"""


# 加密
def encrypt(message):
    crypt = ""
    for i in message:
        code = ord(i)
        crypt += str(code) + "|"
    return crypt


# 解密
def decrypt(crypt):
    result = ""
    if crypt:
        result_list = crypt.split("|")
        result_list.remove("")
        for i in result_list:
            char = chr(int(i))
            result += char
    return result


if __name__ == "__main__":
    msg = "人生苦短， 我用Python～～～～"
    crypt = encrypt(message=msg)
    print(crypt)
    decrypt = decrypt(crypt)
    print(decrypt)
