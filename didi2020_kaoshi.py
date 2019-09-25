#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/18 17:57
@File    : zhuanzhuan2020mianshi
@Software: PyCharm
"""

def call(str1, n, k):
    result = "0" * (k - 1)
    for i in range(k-1, len(str1)):
        flag = 0
        if (i+1) % k == 0:
            t = (i+1) // k
            B = str1[:t]
            if str1[:i+1] == (t+1) * B:
                result += "1"
                flag = 1
        if (i+1) % (k+1) == 0:
            t = (i+1) // (k+1)
            A = str1[:t]
            if str1[:i + 1] == (t+1) * A:
                result += "1"
                flag = 1
        if (i+1) % (2*k+1) == 0:
            t = (i+1) // (2*k+1)
            A = str1[:t]
            B = str1[t+1: 2*t+1]
            if str1[:i + 1] == (t+1)* (A+B):
                result += "1"
                flag = 1
        if not flag:
            result += "0"
    return result
if __name__ == '__main__':
    n, k = list(map(int, input().split(" ")))
    str1 = input()
    print(call(str1, n, k))
