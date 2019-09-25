#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/18 9:42
@File    : meituan2019_dota2
@Software: PyCharm
"""
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = int(input())
        n, d, x, y = list(map(int, input().split(" ")))
        t0, t1, t2 = list(map(int, input().split(" ")))
        t = 0
        flag = False
        while 1:
            if t % t0 == 0:
                s -= n * d
            if s <= 0:
                flag = False
                break
            if t % t1 == 0:
                s -= y
            if t % t2 == 0:
                s -= x
            if s <= 0:
                flag = True
                break
            t += 1
        if flag: print("YES")
        else: print("NO")