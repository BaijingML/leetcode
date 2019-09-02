#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 18:49
@File    : shunfeng2020_test
@Software: PyCharm
"""
if __name__ == "__main__":
    n ,m, k = input().split(" ")
    n, m, k = int(n), int(m), int(k)
    temp = [set() for _ in range(m)]
    for i in range(k):
        u, v = input().split(" ")
        u, v = int(u), int(v)
        temp[v-1].add(u)
    te = [i for i in temp if i]
    ts = te[0]
    su = set(i for i in range(1, m+1))
    count = 0
    if len(te) < 1:
        print(0)
    elif len(te) == 1:
        for i in range(1, m+1):
            if i not in te[0]:
                count += 1
    else:
        ts = te[0]
        for i in range(1, len(te)):
            if te[i-1] & te[i]:
                continue
            else:
                for j in range(1, m+1):
                    if j not in te[i]:
                        te[i].add(j)
                        count += 1
                        ts = te[i] | ts
                        if te[i-1] & te[i] or ts == su:
                            break
                if not (te[i-1] & te[i]):
                    count += 1
    print(count)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split(" ")))
    temp = [nums[0]]
    result = 1
    if n > 2:
        for i in range(1, n):
            left = 0
            right = len(temp)
            while left < right:
                mid = (left + right) >> 1
                if temp[mid] <= nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if left == len(temp):
                temp.append(nums[i])
            else:
                temp[left] = nums[i]
        print(len(temp))
    else:
        print(n)


