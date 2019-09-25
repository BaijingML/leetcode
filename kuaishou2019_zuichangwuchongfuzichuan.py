#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/24 21:33
@File    : kuaishou2019_zuichangwuchongfuzichuan
@Software: PyCharm
"""
if __name__ == '__main__':
    str1 = input()
    maxl = 0
    currentl = 0
    s = {}
    for i in range(len(str1)):
        # print(currentl)
        if str1[i] not in s.keys():
            currentl += 1
            s[str1[i]] = i
        else:
            currentl = i - s[str1[i]]
            s[str1[i]] = i
        maxl = max(maxl, currentl)
    print(maxl)