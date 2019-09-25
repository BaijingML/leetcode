#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/18 10:55
@File    : meituan2019_manjian
@Software: PyCharm
"""
if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))
    minvalue = min(nums)
    maxvalue = max(nums)
    print(nums, minvalue, maxvalue, len(nums))
    temp = [0] * (maxvalue - minvalue + 1)
    for i in range(m):
        left, right = list(map(int, input().split(" ")))
        # print(left, right)
        if left > maxvalue or right < minvalue:
            continue
        elif left <= minvalue and right >= maxvalue:
            temp[0] += 1
            temp[maxvalue - minvalue] -= 1
        elif left >= minvalue and right <= maxvalue:
            temp[left-minvalue] += 1
            temp[right-minvalue] -= 1
        elif left >= minvalue and right > maxvalue:
            temp[left-minvalue] += 1
            temp[maxvalue-minvalue] -= 1
        elif left == right:
            continue
    count = 0
    for i in temp:
        if i == 0:
            print(count)
        elif i > 0:
            count += i
            print(count)
        elif i < 0:
            print(count)
            count -= 1


