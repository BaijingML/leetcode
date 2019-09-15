#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/8 18:38
@File    : aiqiyi2020
@Software: PyCharm
"""
if __name__ == '__main__':
    X, Y, Z, k = list(map(int, input().split(" ")))
    x, y, z = 1, 1, 1
    t = 0
    while k > 0 and (x < X or y < Y or z < Z):
        k -= 1
        print(x, y, z)
        if x < X and y < Y and z < Z:
            t = max((x+1)*y *z, x*(y+1)*z, x*y*(z+1))
        elif y < Y and z < Z:
            t = max(x*(y+1)*z, x*y*(z+1))
        elif x < X and y < Y:
            t = max((x+1)*y *z, x*(y+1)*z)
        elif x < X and z < Z:
            t = max((x+1)*y *z, x*y*(z+1))
        elif x < X:
            t = (x+1)*y *z
        elif y < Y:
            t = x*(y+1)*z
        else:
            t = x*y*(z+1)
        if t == (x+1)*y *z and x < X:
            x += 1
        elif t == x*(y+1)*z and y < Y:
            y += 1
        else:
            z += 1
    print(t)

