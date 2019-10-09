#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/8 16:16
@File    : No260 Single Number III
@Software: PyCharm
"""
class Solution:
    def singleNumber(self, nums):
        temp = 0
        for i in nums:
            temp ^= i
        flag = 1
        while (temp & 1) == 0:
            flag <<= 1
            temp >>= 1
        left, right = [], []
        for i in nums:
            if i & flag == 0:
                left.append(i)
            else:
                right.append(i)
        # print(flag, left, right)
        result = [0, 0]
        for i in left:
            result[0] ^= i
        for j in right:
            result[1] ^= j
        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.singleNumber([1,2,1,3,2,5]))