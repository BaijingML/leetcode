#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/12 14:51
@File    : qunaer2020_kaoshi
@Software: PyCharm
"""
def get_matrix(nums, n):
    temp_sum = 0
    for i in range(n):
        arr = [0 for _ in range(n)]
        for j in range(i, n):
            for k in range(n):
                arr[k] += nums[j][k]
                temp_max = maxsum(n, arr)
                if temp_max > temp_sum:
                    temp_sum = temp_max

    return temp_sum

def maxsum(n, arr):
    sum1 = 0
    b = 0
    for i in range(n):
        if b > 0:
            b += arr[i]
        else:
            b = arr[i]
        if b > sum1:
            sum1 = b
    return sum1


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(" ")))
    temp = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(nums[i*n+j])
        temp.append(t)
    print(get_matrix(temp, n))
