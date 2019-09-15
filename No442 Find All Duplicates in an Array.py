#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 16:37
@File    : No442 Find All Duplicates in an Array
@Software: PyCharm
"""
class Solution:
    def findDuplicates(self, nums):
        result = []
        for i in nums:
            t = abs(i) - 1
            if nums[t] < 0:
                result.append(abs(i))
            else:
                nums[t] = -nums[t]
        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.findDuplicates([4,3,2,7,8,2,3,1]))