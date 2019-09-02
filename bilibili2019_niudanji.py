#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/27 19:34
@File    : bilibili2019_niudanji
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    result = ""
    while N >= 1:
        if (N - 1) % 2 == 0:
            result += "2"
            N = (N - 1) / 2
        else:
            result += "3"
            N = (N - 2) / 2
    print(result[::-1])
