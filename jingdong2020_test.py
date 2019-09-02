#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/24 18:55
@File    : jingdong2020_test
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    nums = input()
    temp = [[0, 0, 0] for _ in range(N)]
    if ord(nums[0]) >= ord("a"):
        temp[0][0] = 1
        temp[0][1] = 3
        temp[0][2] = 3
    else:
        temp[0][0] = 2
        temp[0][1] = 2
        temp[0][2] = 2
    for i in range(1, N):
        if ord(nums[i]) >= ord("a"):
            if min(temp[i-1]) == temp[i-1][0]:
                temp[i][0] = temp[i-1][0] + 1
                temp[i][1] = temp[i - 1][1] + 2
            else:
                temp[i][0] = temp[i - 1][0] + 1
            if min(temp[i-1]) == temp[i-1][1]:
                temp[i][1] = temp[i-1][1] + 2
            else:
                temp[i][1] = temp[i - 1][1] + 2
            if min(temp[i-1]) == temp[i-1][2]:
                temp[i][2] = temp[i-1][2] + 2
            temp[i][2] = temp[i-1][2] + 3
        else:
            temp[i][0] = temp[i-1][0] + 2
            temp[i][1] = temp[i-1][1] + 1
            temp[i][2] = temp[i-1][2] + 1
    result = min(temp[N-1])
    print(result)


