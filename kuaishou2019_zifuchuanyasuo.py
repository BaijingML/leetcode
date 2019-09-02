#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/26 22:00
@File    : kuaishou2019_zifuchuanyasuo
@Software: PyCharm
"""
if __name__ == "__main__":
    str1 = input()
    result = ""
    count = 1
    n = len(str1)
    for i in range(1, n):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            result += str(count) + str1[i-1]
            count = 1
    result += str(count) + str1[-1]
    print(result)