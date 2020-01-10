#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2020/1/10 19:52
@File    : No1295 Find Numbers with Even Number of Digits
@Software: PyCharm
"""
class Solution:
    def findNumbers(self, nums):

        return sum([1 for i in nums if len(str(i)) % 2 == 0])

if __name__ == '__main__':
    solu = Solution()
    print(solu.findNumbers([]))