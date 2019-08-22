#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 21:05
@File    : waiqibishi_2020
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    nums = input().split(" ")
    if N <= 2:
        print(0)
    else:
        count = 0
        for i in range(int(2*N)):
            if i % 2 == 0:
                continue
            else:
                if nums[i] == nums[i-1]:
                    continue
                else:
                    for j in range(i+1, int(2*N)):
                        if nums[j] == nums[i-1]:
                            for k in range(j, i, -1):
                                nums[k], nums[k-1] = nums[k-1], nums[k]
                                count += 1
        print(count)
