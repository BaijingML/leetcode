#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 20:33
@File    : No1091 Shortest Path in Binary Matrix
@Software: PyCharm
"""
def shortestPathBinaryMatrix(self, grid):
    m, n = len(grid), len(grid[0])
    temp = [[0 for _ in range(n)] for _ in range(m)]
    if grid[0][0] == 1 or grid[m][n] == 1: return -1
