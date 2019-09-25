#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/17 9:52
@File    : mairui2020
@Software: PyCharm
"""
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(" ")))
    count = 0
    for i in range(n-1):
        count += max(0, nums[i] - nums[i+1])
    print(count + nums[-1])