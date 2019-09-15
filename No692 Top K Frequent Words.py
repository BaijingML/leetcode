#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 19:51
@File    : No692 Top K Frequent Words
@Software: PyCharm
"""

class Solution:
    def topKFrequent(self, words, k):
        d = {}
        for i in words:
            if i in d.keys():
                d[i][0] += 1
            else:
                d[i] = [1, i]
        temp = []
        for i in d.keys():
            temp.append(d[i])
        n = len(temp)
        for i in range(n):
            for j in range(n-1, i, -1):
                if self.compare(temp[j], temp[j-1]):
                    temp[j], temp[j - 1] = temp[j - 1], temp[j]
        res = []
        for i in temp:
            res.append(i[1])
        return res[:k]
    def compare(self, a, b):
        if a[0] > b[0]:
            return True
        elif a[0] == b[0]:
            if a[1] < b[1]:
                return True
            return False
        return False

if __name__ == '__main__':
    solu = Solution()
    print(solu.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))