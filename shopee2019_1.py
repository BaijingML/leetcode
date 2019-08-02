#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/7/30 16:09
@File    : shopee2019
@Software: PyCharm
"""

def count(m, r, c):
    for i in range(1, r):
        for j in range(1, c):
            if m[i][j] == -1:
                continue
            if m[i-1][j] > 0 and m[i][j-1] > 0:
                m[i][j] = m[i][j-1] + m[i - 1][j]
            elif m[i-1][j] < 0 and m[i][j-1] < 0:
                m[i][j] = 0
            elif m[i][j-1] < 0:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = m[i][j-1]
    return m[r-1][c-1 ]


if __name__ == "__main__":
    s = input().split(' ')
    row, column = int(s[0]) + 1, int(s[1]) + 1
    mat = [[1] * column for a in range(row)]
    for j in range(int(s[2])):
        boss = input().split(' ')
        mat[int(boss[0])][int(boss[1])] = -1
    print(count(mat, row, column))
