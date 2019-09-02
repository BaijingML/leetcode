#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 15:02
@File    : kuaishou2019_lianxuzishuzudezuidahe
@Software: PyCharm
"""
if __name__ == "__main__":
    result = 0
    nums = list(map(int, input().split(",")))
    temp = 0
    for i in range(len(nums)):
        if temp + nums[i] > 0:
            temp = temp+nums[i]
        else:
            result = max(temp, result)
            temp = 0
    print(max(0, result, temp))
