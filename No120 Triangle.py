#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 21:11
@File    : No120 Triangle
@Software: PyCharm
"""
class Solution:
    def minimumTotal(self, triangle):
        m = len(triangle)
        if m > 1:
            result = triangle[m-1]
            for i in range(m-2, -1, -1):
                for j in range(len(triangle[i])):
                    result[j] = min(result[j], result[j+1]) + triangle[i][j]
            return result[0]
        else:
            return triangle[0][0]
if __name__ == "__main__":
    solu = Solution()
    print(solu.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
