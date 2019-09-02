#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 21:58
@File    : No72 Edit Distance
@Software: PyCharm
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        temp = [[0 for _ in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            temp[i][0] = i
        for j in range(n+1):
            temp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    temp[i][j] = temp[i-1][j-1]
                else:
                    temp[i][j] = min(temp[i][j-1], temp[i-1][j], temp[i-1][j-1]) + 1
        return temp[m][n]
if __name__ == "__main__":
    solu = Solution()
    print(solu.minDistance("horse", "ros"))
