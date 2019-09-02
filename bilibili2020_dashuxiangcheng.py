#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 21:34
@File    : bilibili2020_dashuxiangcheng
@Software: PyCharm
"""
if __name__ == "__main__":
    N, M = input().split(" ")
    m, n = len(M), len(N)
    temp = [0 for i in range(m+n)]
    for i in range(m):
        for j in range(n):
            temp[m-i-1+n-j-1] += int(M[i]) * int(N[j])
    for i in range(m+n-1):
        if temp[i] >= 10:
            temp[i+1] += temp[i] // 10
            temp[i] = temp[i] % 10
    temp = temp[::-1]
    if temp[0] == 0:
        del temp[0]
    res = ""
    for i in temp:
        res += str(i)
    print(res)
