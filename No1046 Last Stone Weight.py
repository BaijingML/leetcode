#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/3 22:54
@File    : No1046 Last Stone Weight
@Software: PyCharm
"""
class Solution:
    def lastStoneWeight(self, stones):
        n = len(stones)
        while n > 1:
            temp1 = max(stones)
            stones.remove(temp1)
            temp2 = max(stones)
            if temp1 == temp2:
                stones.remove(temp2)
            else:
                stones.append(temp1 - temp2)
                stones.remove(temp2)
            n = len(stones)
        if n == 1:
            return stones[0]
        else:
            return 0
if __name__ == '__main__':
    solu = Solution()
    print(solu.lastStoneWeight([2]))