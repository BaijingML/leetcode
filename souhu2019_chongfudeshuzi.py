#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/22 20:59
@File    : souhu2019_chongfudeshuzi
@Software: PyCharm
"""
if __name__ == "__main__":
    nums = list(map(int, input().split(" ")))
    n = len(nums) - 1
    print(int(sum(nums) - n*(n-1) / 2))
