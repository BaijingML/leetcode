#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 20:14
@File    : Np279 Perfect Squares
@Software: PyCharm
"""
import math
import sys
class Solution:

    def __init__(self):
        self.dp = [0]

    dp = [0] # so now dp is a class variable
    def numSquares(self, n):
        for i in range(len(self.dp), n+1):
            result = sys.maxsize
            k = int(math.sqrt(i))
            if k * k == i:
                self.dp.append(1)
                continue
            for j in range(1, int(math.sqrt(i)) + 1):
                result = min(result, self.dp[i - j * j] + 1)
                if result is 2:
                    break
            self.dp.append(result)
        return self.dp[n]