#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/8 19:44
@File    : No797 All Paths From Source to Target
@Software: PyCharm
"""
class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        self.dsf(graph, result, 0, [0])
        return result
    def dsf(self, g, res, pos, path):
        if pos == len(g) - 1:
            res.append(path)
            return
        else:
            for j in g[pos]:
                self.dsf(g, res, j, path+[j])
if __name__ == '__main__':
    solu = Solution()
    print(solu.allPathsSourceTarget([[1,2], [3], [3], []] ))