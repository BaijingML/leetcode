#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/25 9:58
@File    : xiaomi2020_mianshi
@Software: PyCharm
"""
import heapq
if __name__ == '__main__':
    d = {}
    with open("D://1.txt", "r") as f:
        content = f.readlines()
        for line in content:
            if line not in d.keys():
                d[line] = [1, line]
            else:
                d[line][0] += 1
    temp = []
    for i in d.keys():
        heapq.heappush(temp, d[i])
    result = [i[1] for i in heapq.nlargest(5, temp)]
    print(result)