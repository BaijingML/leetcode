#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/24 21:30
@File    : kuaishou2019_zifuchuanpaixu
@Software: PyCharm
"""
if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        temp = input()[-6:]
        nums.append(int(temp))
    nums.sort()
    for i in nums:
        print(i)
