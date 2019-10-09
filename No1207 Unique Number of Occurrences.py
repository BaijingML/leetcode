#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/4 0:13
@File    : No1049 Last Stone Weight II
@Software: PyCharm
"""
class Solution:
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        return len(d) == len(set(d.values()))

if __name__ == '__main__':
    solu = Solution()
    print(solu.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))