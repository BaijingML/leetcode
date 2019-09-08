#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/3 15:43
@File    : xiaomi2019_zichanbaodabao
@Software: PyCharm
"""
if __name__ == "__main__":
    V, N, W, Values = input().split(",")
    V, N = int(V), int(N)
    W = list(map(int, W.split(" ")))
    values = list(map(int, Values.split(" ")))
    temp = [[0 for i in range(V+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, V+1):
            if W[i-1] > j:
                temp[i][j] = temp[i-1][j]
            else:
                temp[i][j] = max(temp[i-1][j-W[i-1]] + values[i-1], temp[i-1][j])
    print(temp[N][V])