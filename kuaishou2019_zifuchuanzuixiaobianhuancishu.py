#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/26 16:19
@File    : 快手
@Software: PyCharm
"""
if __name__ == "__main__":
    str1, str2 = input(), input()
    str1 = "*" + str1
    str2 = "*" + str2
    result = [[0 for i in range(len(str2))] for j in range(len(str1))]
    for i in range(len(str1)):
        result[i][0] = i
    for j in range(len(str2)):
        result[0][j] = j
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = min(result[i-1][j], result[i][j-1], result[i-1][j-1]) + 1
    print(result[len(str1)-1][len(str2)-1])

