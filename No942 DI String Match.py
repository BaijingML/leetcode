#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 16:47
@File    : No942 DI String Match
@Software: PyCharm
"""
class Solution:
    def diStringMatch(self, S):
        low, high = 0, len(S)
        result = [0] * (high + 1)
        for i in range(len(S)):
            if S[i] == "D":
                result[i] = high
                high -= 1
            else:
                result[i] = low
                low += 1
        result[-1] = low
        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.diStringMatch("D"))