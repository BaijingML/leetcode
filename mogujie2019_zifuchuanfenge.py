#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/24 22:03
@File    : mogujie2019_zifuchuanfenge
@Software: PyCharm
"""
"""
合并多个相交的区间，取出合并后每个不相交取间的长度
"""
if __name__ == '__main__':
    str1 = input()
    temp = [[-1, -1] for _ in range(26)]
    for i in range(len(str1)):
        if temp[ord(str1[i]) - ord("a")][0] == -1:
            temp[ord(str1[i]) - ord("a")][0] = i
        temp[ord(str1[i]) - ord("a")][1] = i
    temp.sort(key = lambda x:x[0])
    left, right = 0, 0
    result = []
    for i in range(26):
        if temp[i][0] == -1:
            continue
        if temp[i][0] > right:
            result.append(right - left + 1)
            left = temp[i][0]
        right = max(right, temp[i][1])
    result.append(right - left + 1)
    print(" ".join(map(str, result)))

