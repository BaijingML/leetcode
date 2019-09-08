#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/4 23:19
@File    : xiaomi2019_lianggezhichuxianyici
@Software: PyCharm
"""
def getNumber(nums):
    t = 0
    for i in nums:
        t = t ^ i
    index = 0
    a, b = 0, 0
    while (t  & 1) == 0:
        t = t >> 1
        index += 1
    for i in nums:
        if ((i >> index) & 1) == 1:
            a = a ^ i
        else:
            b = b ^ i
    return a, b
if __name__ == "__main__":
    arr = []
    while True:
        try:
            arr.append(int(input()))
        except:
            break
    a, b = getNumber(arr)
    if a < b:
        print(a, b)
    else:
        print(b, a)


