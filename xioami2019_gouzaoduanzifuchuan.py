#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 16:02
@File    : xioami2019_gouzaoduanzifuchuan
@Software: PyCharm
"""
def call(str1, str2):
    d = {}
    for i in str2:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for j in str1:
        if j in d.keys():
            if d[j] >= 1:
                d[j] -= 1
            else:
                return False
        else:
            return False
    return True
if __name__ == "__main__":
    str1, str2 = input().split(" ")
    if call(str1, str2):
        print("true")
    else:
        print("false")
