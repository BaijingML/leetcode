#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 19:38
@File    : No547 Friend Circles
@Software: PyCharm
"""
class Solution:
    def findCircleNum(self, M):
        m = len(M)
        leader = [i for i in range(m)]
        group = m
        for i in range(m-1):
            for j in range(i+1, m):
                if M[i][j]:
                    leader1 = self.findleader(i, leader)
                    leader2 = self.findleader(j, leader)
                    if leader1 != leader2:
                        leader[leader1] = leader2
                        group -= 1
        return group

    def findleader(self, k, leader):
        if k == leader[k]:
            return k
        return self.findleader(leader[k], leader)

if __name__ == '__main__':
    solu = Solution()
    print(solu.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
