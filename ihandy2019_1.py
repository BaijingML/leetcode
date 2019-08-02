#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/7/30 21:40
@File    : ihandy2019_1
@Software: PyCharm
"""
from functools import cmp_to_key
def compare(a, b):
    if int(a+b) > int(b+a):
        return -1
    elif int(a+b) < int(b+a):
        return 1
    else:
        return 0

if __name__ == "__main__":
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(str(input()))
    print(mat)
    mat.sort(key=cmp_to_key(compare))
    result = ''.join(mat)
    print(int(result))