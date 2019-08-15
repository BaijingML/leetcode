#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/15 10:45
@File    : No96 Unique Binary Search Trees
@Software: PyCharm
"""
class Solution:
    def numTrees(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                nums[i] +=  nums[j] * nums[i-j-1]
        return nums[n]