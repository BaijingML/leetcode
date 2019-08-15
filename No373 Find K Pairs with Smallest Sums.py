#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/13 22:52
@File    : No373 Find K Pairs with Smallest Sums
@Software: PyCharm
"""
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_temp = []
        if not nums1 or not nums2:
            return []
        heappush(min_temp, (nums1[0]+nums2[0], [nums1[0], nums2[0]], 0, 0))
        result = []
        if k < len(nums1) * len(nums2):
            while k > 0:
                temp, ret, m, n = heappop(min_temp)
                result.append(ret)
                if m == 0 and n + 1 < len(nums2):
                    heappush(min_temp, (nums1[0]+nums2[n+1], [nums1[0], nums2[n+1]], m, n+1))
                if m +1 < len(nums1):
                    heappush(min_temp, (nums1[m+1]+nums2[n], [nums1[m+1], nums2[n]], m+1, n))
                k -= 1
            return result
        else:
            return [[i, j] for i in nums1 for j in nums2]