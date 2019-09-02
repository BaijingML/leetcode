#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/30 22:16
@File    : souhu2019_sushudeduishu
@Software: PyCharm
"""
def zhishu(n):
    temp = []
    for i in range(2, n + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            temp.append(i)
    return temp

if __name__ == "__main__":
    import math
    n = int(input())
    temp = zhishu(n)
    left, right = 0, len(temp)-1
    count = 0
    while left <= right:
        if temp[left] + temp[right] == n:
            count += 1
            right -= 1
            left += 1
        elif temp[left] + temp[right] > n:
            right -= 1
        else:
            left += 1
    print(count)

