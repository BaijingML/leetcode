#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 20:14
@File    : zhaoyinxinyongka2020
@Software: PyCharm
"""

if __name__ == '__main__':
    l, r = list(map(int, input().split(" ")))
    min_v = float("inf")
    for i in range(l, r):
        for j in range(i+1, r+1):
            min_v = min(i * j % 2019, min_v)
    print(min_v)

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(" ")))
    de = list(map(int, input().split(" ")))
    result = 0
    left = 0
    for i in range(n):
        if de[i] + left >= nums[i]:
            result += nums[i]
            if left >= nums[i]:
                left = de[i]
            else:
                left = de[i] + left - nums[i]
        else:
            result += de[i] + left
            left = 0
    result += min(nums[n], left)
    print(result)


if __name__ == '__main__':
    n = int(input())
    info = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    while True:
        try:
            p, c, v = list(map(int, input().split(" ")))
            info[p][c] = v
        except:
            break
    d = {i:0 for i in range(1, n+1)}
    for i in range(n+1, 0, -1):
        for j in range(i+1, n+1):
            dp[i] = max(dp[i], dp[j] + info[i][j])
    for i in range(n):
        print(dp[i+1], end = " ")

