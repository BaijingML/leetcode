#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/3 14:13
@File    : xiaomi2019_xiaomingdezifuchuan
@Software: PyCharm
"""
if __name__ == "__main__":
    N, T = list(map(int, input().split(" ")))
    str1 = input()
    info = []
    n = len(str1)
    for i in range(T):
        type, X = list(map(int, input().split(" ")))
        if type == 1:
            str1 = str1[n-X:] + str1[:n-X]
        else:
            print(str1[X])
