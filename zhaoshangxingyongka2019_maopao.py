#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/22 19:24
@File    : zhaoshangxingyongka2019
@Software: PyCharm
"""
if __name__ == "__main__":
    s = list(input())
    n = len(s)
    if n <= 2:
        print(0)
    else:
        count = 0
        for i in range(n):
            for j in range(n-i-1):
                if s[j] > s[j+1]:
                    count += 1
                    s[j], s[j+1] = s[j+1], s[j]
        print(count)


