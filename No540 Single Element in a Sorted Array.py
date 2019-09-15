#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 18:49
@File    : No540 Single Element in a Sorted Array
@Software: PyCharm
"""
class Solution:
    def singleNonDuplicate(self, nums):
        mid = int(len(nums) / 2)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    left = mid + 1
            mid = int((left + right) / 2)
        return nums[left]
if __name__ == '__main__':
    solu = Solution()
    print(solu.singleNonDuplicate([1,1,2,3,3]))