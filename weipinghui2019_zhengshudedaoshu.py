#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/30 22:11
@File    : weipinghui2019_zhengshudedaoshu
@Software: PyCharm
"""
if __name__ == "__main__":
    n = input()
    if n[0] == "-":
        s = n[1:]
        print(s)
        print("-"+s[::-1])
    elif n == "0":
        print("0")
    else:
        print(n[::-1])