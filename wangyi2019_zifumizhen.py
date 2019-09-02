#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 16:32
@File    : wangyi2019_zifumizhen
@Software: PyCharm
"""
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n = input().split(" ")
        m, n = int(m), int(n)
        info = []
        for i in range(m):
            info.append(input())
        target = input()
        l = len(target)
        count = 0
        for i in range(m):
            for j in range(n):
                if info[i][j] == target[0]:
                    for k in range(1, l):
                        if i+k >= m:
                            break
                        if info[i+k][j] != target[k]:
                            break
                        if k == l-1:
                            count += 1
                    for k in range(1, l):
                        if j+k >= n:
                            break
                        if info[i][j+k] != target[k]:
                            break
                        if k == l - 1:
                            count += 1
                    for k in range(1, l):
                        if i+k >= m or j+k >= n:
                            break
                        if info[i+k][j+k] != target[k]:
                            break
                        if k == l - 1:
                            count += 1
        print(count)

