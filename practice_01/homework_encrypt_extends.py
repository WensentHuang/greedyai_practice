#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -------------------------------
# Name:          homework_encrypt_extends
# Description:
# Author:        yinxi
# Date:          2019-08-04
# -------------------------------

"""
扩展加密解密程序
加密规则： 字符串，拼上一串指定的字符串，后获取ascii码，以|分割
"""


# 加密
def encrypt(message, iv):
    """
    这种方式加密也会存在一些问题，如果iv较短，并且与要加密的字符串有重复，则解密出来的字符串会错误，故iv应尽量使用随机字符串
    :param message: 要加密的字符串
    :param iv: 随机串
    :return: 加密串
    """
    result = ""
    new_message = message + iv
    for i in new_message:
        code = ord(i)
        result += str(code) + "|"
    return result


# 解密
def decrypt(crypt, iv):
    result = ""
    iv_string = ""
    if crypt:
        for i in iv:
            code = ord(i)
            iv_string += str(code) + "|"
        new_crypt = crypt.split(iv_string)[0]
        # 若iv与原始的字符串一致
        if not new_crypt:
            new_crypt = iv_string
        new_crypt_list = new_crypt.split("|")
        new_crypt_list.remove("")
        for i in new_crypt_list:
            char = chr(int(i))
            result += char
    return result


if __name__ == "__main__":
    message = "人生苦短， 我用Python！！！～～～"
    iv = "cxk"
    crypt = encrypt(message=message, iv=iv)
    print("加密后的字符串：", crypt)
    decrypt = decrypt(crypt=crypt, iv=iv)
    print("解密后的字符串：", decrypt)
