#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/26 22:25
@File    : bilibili2019_luxiandedaijia
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(map(int, input().split(","))))
    result = [[0 for i in range(N)] for j in range(N)]
    result[0][0] = temp[0][0]
    for i in range(1, N):
        result[i][0] = temp[i][0] + result[i-1][0]
    for j in range(1, N):
        result[0][j] = temp[0][j] + result[0][j-1]
    for i in range(1, N):
        for j in range(1, N):
            result[i][j] = min(result[i-1][j], result[i][j-1]) + temp[i][j]
    print(result[N-1][N-1])


