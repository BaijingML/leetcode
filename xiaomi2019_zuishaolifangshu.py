#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/5 9:42
@File    : xiaomi2019_zuishaolifangshu
@Software: PyCharm
"""
import math
if __name__ == "__main__":
    n = int(input())
    m = int(math.ceil(n ** (1/3)))
    temp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        temp[1][i] = i
    for i in range(2, m+1):
        for j in range(n+1):
            if j >= i ** 3:
                temp[i][j] = min(temp[i-1][j-i**3]+1, temp[i-1][j], temp[i][j-i**3] + 1)
            else:
                temp[i][j] = temp[i-1][j]
    print(temp[m][n])

