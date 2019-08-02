#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/7/30 16:59
@File    : shopee2019_2
@Software: PyCharm
"""
def count(nums, m):
    row = 0
    column = 0
    S = 0
    for i in range(m):
        for j in range(m):
            if nums[i][j] == 1:
                row += i
                column += j
                S += 1
    if S == m ** 2:
        return -1
    else:
        k = row / S
        l = column / S
    min_record, p, q = m*2, 0, 0
    for i in range(m):
        for j in range(m):
            if nums[i][j] == 0:
                temp = abs(i-k) + abs(j-l)
                if temp < min_record:
                    min_record = temp
                    p, q = i, j
    print(p, q)
    res = 0
    for i in range(m):
        for j in range(m):
            if nums[i][j] == 1:
                res += abs(i-p) + abs(j-q)
    return res

if __name__ == "__main__":
    L = int(input())
    mat = []
    for i in range(L):
        mat.append(input().split(' '))
    print(mat)
    for i in range(L):
        for j in range(L):
            mat[i][j] = int(mat[i][j])
    print(count(mat, L))
