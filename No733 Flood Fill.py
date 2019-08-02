#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/2 11:34
@File    : No733 Flood Fill
@Software: PyCharm
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        if not m: return []
        n = len(image[0])
        def expand(r, c):
            if image[r][c] == start_color:
                image[r][c] = newColor
                if r >= 1: expand(r-1, c)
                if r < m-1: expand(r+1, c)
                if c >= 1: expand(r, c-1)
                if c < n-1: expand(r, c+1)
        start_color = image[sr][sc]
        if start_color == newColor: return image
        expand(sr, sc)
        return image