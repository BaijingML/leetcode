#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/24 10:27
@File    : kuaishou2019_zuidagongognzichuan
@Software: PyCharm
"""
if __name__ == "__main__":
    str1, str2 = input().split(",")
    temp = [[0 for j in range(len(str2))] for i in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if temp[i-1][j-1] > 0:
                    temp[i][j] = temp[i-1][j-1] + 1
                else:
                    temp[i][j] = 1
    m = -float("inf")
    for i in range(len(str1)):
        for j in range(len(str2)):
            if temp[i][j] > m:
                m = temp[i][j]
            else:
                continue
    print(m)