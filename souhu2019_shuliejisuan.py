#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/24 9:27
@File    : souhu2019_shuliejisuan
@Software: PyCharm
"""
if __name__ == "__main__":
    N, K = list(map(int, input().split(" ")))
    kb_str = bin(K)[2:][::-1]  # 如bin(5)-->'0b101'
    t = 0
    res = 0
    for i in range(len(kb_str)):
        if kb_str[i] == "1":
            res += pow(N, t)
        t += 1
    print(res)
