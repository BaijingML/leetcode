#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/17 15:07
@File    : pingduoduo2020
@Software: PyCharm
"""
def dsf(s, current, step):
    # if step == n+1:
    #     if s == m and current == step:
    #         return 1
    #     else:
    #         return 0
    # temp = current
    # if current > 9:
    #     temp = current // 10
    # if temp == 1:
    #     return dsf(s+current, step+1, step + 1) + dsf(s, current*10 +step + 1, step + 1)
    # else:
    #     return dsf(s+current, step+1, step + 1) + dsf(s, current*10 +step + 1, step + 1) + dsf(s-current, step+1, step + 1)
    step += 1
    if A == B:
        return step
    elif A * 10 + 1 <= B:
        return dsf(A * 10 + 1, step)
    elif A * 2 <= B:
        return dsf(A * 2, step)
    elif A * 10 + 1 > B:
        return -1

if __name__ == '__main__':
    A, B = list(map(int, input().split(" ")))
    count = 0
    print(dsf(A, 0))