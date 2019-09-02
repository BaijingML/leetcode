#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/22 21:10
@File    : zhaoshangxinyongka2019_zuixiaobushu
@Software: PyCharm
"""

if __name__ == "__main__":
    M = int(input())
    k = 0
    s = 0
    while s < M:
        k += 1
        s += k
    dt = s - M
    if dt % 2 == 0:
        print(k)   # 1,2
    else:
        if k % 2 == 0:
            print(k+1) # 3,4
        else:
            print(k + 2)  # 5



