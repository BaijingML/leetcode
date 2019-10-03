#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/25 9:29
@File    : kuaishou2019_zifuchuanchangdudezuidachengji
@Software: PyCharm
"""
if __name__ == '__main__':
    str1 = input()[1:-1].replace("\"", "").split(",")
    temp = [set(i) for i in str1]
    maxl = 0
    for i in range(len(str1)-1):
        for j in range(i+1, len(str1)):
            if temp[i] & temp[j]:
                continue
            else:
                maxl = max(maxl, len(str1[i]) * len(str1[j]))
    print(maxl)

