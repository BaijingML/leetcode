#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 17:17
@File    : xiaomi2019_zichandabao
@Software: PyCharm
"""
12,3,4 5 7,500 600 800
if __name__ == "__main__":
    from collections import OrderedDict
    N, M, d, v = input().split(",")
    N, M  = int(N), int(M)
    d = d.split(" ")
    v = v.split(" ")
    p = {}
    for i in range(M):
        p[int(d[i])] = int(v[i])
    total = 0
