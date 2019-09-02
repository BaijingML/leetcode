#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 15:10
@File    : kuaishou2019_zuishaoshuliangzhuangxiangwenti
@Software: PyCharm
"""
if __name__ == "__main__":
    result = 0
    N = int(input())
    if N == 1 or N == 2 or N == 4:
        print(-1)
    else:
        result += N // 7
        N = N % 7
        if N == 1 or N == 3 or N == 5:
            result += 1
        if N == 2 or N == 4 or N == 6:
            result += 2
        print(result)