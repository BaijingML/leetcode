#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/3 15:58
@File    : VIPKID2020_kaoshi
@Software: PyCharm
"""
# if __name__ == "__main__":
#     N = int(input())
#     count = 0
#     while N > 0 :
#         count += 1
#         N = N & (N-1)
#     print(count)

if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == 0:
            count += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] > 0:
            right -= 1
        else:
            left += 1
    print(count)