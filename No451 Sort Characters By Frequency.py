#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 17:20
@File    : No451 Sort Characters By Frequency
@Software: PyCharm
"""

import heapq
class Solution:
    def frequencySort(self, s):
        result = ""
        d = {}
        for i in s:
            if i in d.keys():
                d[i][0] -= 1
            else:
                d[i] = [-1, i]
        t = []
        for j in d.keys():
            heapq.heappush(t, d[j])
        while t:
            i = heapq.heappop(t)
            result += i[1] * (-i[0])
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.frequencySort("tree"))

