#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/18 11:40
@File    : xiaomi2019_tianshu
@Software: PyCharm
"""
# 田鼠在矩阵中能在K步内走出的方法数
def expand(x, y, K):
    result = 0
    if K > 0:
        if 0 < x: result += expand(x - 1, y, K - 1)
        if x < m - 1: result += expand(x + 1, y, K - 1)
        if 0 < y: result += expand(x, y - 1, K - 1)
        if y < n-1: result += expand(x, y + 1, K - 1)
        if x == 0: result += 1
        if y == 0: result += 1
        if x == m - 1: result += 1
        if y == n - 1: result += 1

        return result
    return 0
if __name__ == "__main__":
    m, n, x, y, K = int(input()), int(input()), int(input()), int(input()), int(input())
    if K < 1:
        print(0)
    else:
        result = expand(x, y, K)
        print(result)