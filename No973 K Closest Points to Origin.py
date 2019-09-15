#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 20:20
@File    : No973 K Closest Points to Origin
@Software: PyCharm
"""
import heapq
class Solution:
    def kClosest(self, points, K):
        temp = []

        for i in points:
            d = i[0] ** 2 + i[1] ** 2
            heapq.heappush(temp, [d, i])
        res = heapq.nsmallest(K, temp)
        result = [i[1] for i in res]
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.kClosest([[3,3],[5,-1],[-2,4]], 2))