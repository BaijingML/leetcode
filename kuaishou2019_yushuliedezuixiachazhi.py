#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/22 20:51
@File    : kuaishou2019_yushuliedezuixiachazhi
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    left = 1
    right = 1
    t = 0
    while t < N:
        t = left + right
        left = right
        right = t
    print(min(abs(left-N), abs(t-N)))