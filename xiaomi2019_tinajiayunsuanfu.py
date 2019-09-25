#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/24 21:10
@File    : xiaomi2019_tinajiayunsuanfu
@Software: PyCharm
"""
def dsf(s, current, step):
    if step == n+1:
        if s == m and current == step:
            return 1
        else:
            return 0
    temp = current
    if current > 9:
        temp = current // 10
    if temp == 1:
        return dsf(s+current, step+1, step + 1) + dsf(s, current*10 +step + 1, step + 1)
    else:
        return dsf(s+current, step+1, step + 1) + dsf(s, current*10 +step + 1, step + 1) + dsf(s-current, step+1, step + 1)

if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    count = 0
    print(dsf(0, 1, 1))
