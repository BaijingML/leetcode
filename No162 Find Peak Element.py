#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/2 12:04
@File    : No162 Find Peak Element
@Software: PyCharm
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1: return 0
        left = 0
        right = n - 1
        while (left < right):
            mid = int((left + right) / 2)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

