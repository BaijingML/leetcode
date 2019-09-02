#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/26 22:39
@File    : bilibili2019_fenpeitangguomanzuweikou
@Software: PyCharm
"""
if __name__ == "__main__":
    target = list(map(int, input().split(" ")))
    value = list(map(int, input().split(" ")))
    target.sort()
    value.sort()
    m, n = len(target), len(value)
    p1, p2 = 0, 0
    count = 0
    while p1 < m and p2 < n:
        if target[p1] <= value[p2]:
            count += 1
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    print(count)
