#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 20:02
@File    : No931 Minimum Falling Path Sum
@Software: PyCharm
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        nums = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            nums[0][i] = A[0][i]
        if m > 1:
            for i in range(1, m):
                for j in range(n):
                    if j == 0:
                        nums[i][j] = min(nums[i-1][j], nums[i-1][j + 1]) + A[i][j]
                    elif j == n-1:
                        nums[i][j] = min(nums[i-1][j], nums[i-1][j - 1]) + A[i][j]
                    else:
                        nums[i][j] = min(nums[i-1][j-1], nums[i-1][j], nums[i-1][j+1]) + A[i][j]
        return min(nums[m-1])

