#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/18 14:47
@File    : meituan2020_kaoishi
@Software: PyCharm
"""
if __name__ == '__main__':
    info = input()
    if len(info) < 1:
        print(0)
    else:
        nums = list(map(int, info.split(",")))
        count = 0
        new = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != new[i]:
                count +=1
        print(count)
# def long(nums):
#     result = 0
#     temp = [{} for i in range(len(nums))]
#     for i in range(len(nums)):
#         for j in range(i):
#             diff = nums[i] - nums[j]
#             if diff in temp[j]:
#                 temp[i][diff] = temp[j][diff] + 1
#             else:
#                 temp[i][diff] = 2
#             result = max(result, temp[i][diff])
#     return result
# if __name__ == '__main__':
#     info = input()
#     if len(info) < 1:
#         print(0)
#     else:
#         nums = list(map(int, info.split(",")))
#         if len(nums) == 1:
#             print(1)
#         elif sum(nums) == nums[0] * len(nums):
#             print(len(nums))
#         else:
#             print(long(nums))
            # d = {}
            # for i in range(len(nums)):
            #     for j in range(i+1, len(nums)):
            #         temp = nums[i] - nums[j]
            #         if temp not in d.keys():
            #             d[temp] = [nums[i], nums[j]]
            #         elif d[temp][-1] == nums[j]:
            #             d[temp].append(nums[j])
            # result = 0
            # for i in d.keys():
            #     if len(d[i]) > result:
            #         result = len(d[i])
            # print(result)