#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/27 19:53
@File    : meituan2019_kaoshicelue
@Software: PyCharm
"""
if __name__ == "__main__":
    M = int(input())
    temp = []
    for i in range(M):
        temp.append(list(map(int, input().split(" "))))
    t = 120
    result = [[0 for _ in range(121)] for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(121):
            if temp[i-1][0] <= j < temp[i-1][2]:
                result[i][j] = max(result[i-1][j], result[i-1][j-temp[i-1][0]] + temp[i-1][1])
            elif j >= temp[i-1][2]:
                result[i][j] = max(result[i-1][j], result[i-1][j-temp[i-1][0]] + temp[i-1][1],
                                   result[i-1][j-temp[i-1][2]] + temp[i-1][3])
            else:
                result[i][j] = result[i - 1][j]
    print(result[M][120])




