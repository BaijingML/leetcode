#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/27 19:44
@File    : mogujie2019_fanggedezoufa
@Software: PyCharm
"""
if __name__ == "__main__":
    M, N = input().split(" ")
    M, N = int(M)+1, int(N)+1
    result = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        result[i][0] = 1
    for j in range(N):
        result[0][j] = 1
    for i in range(1, M):
        for j in range(1, N):
            result[i][j] = result[i-1][j] + result[i][j-1]
    print(result[M-1][N-1])