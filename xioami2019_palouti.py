#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/4 22:35
@File    : xioami2019_palouti
@Software: PyCharm
"""
if __name__ == "__main__":
    n = int(input())
    result = 0
    left = 1
    right = 2
    if n == 1:
        print(left)
    elif n == 2:
        print(right)
    else:
        for i in range(3, n+1):
            result = left + right
            left = right
            right = result
        print(result)