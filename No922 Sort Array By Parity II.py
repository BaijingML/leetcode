#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 17:20
@File    : No922 Sort Array By Parity II
@Software: PyCharm
"""
class Solution:
    def sortArrayByParityII(self, A):
        result = [0] * len(A)
        even, odd = 0, 1
        for i in A:
            if i % 2 == 0:
                result[even] = i
                even += 2
            else:
                result[odd] = i
                odd += 2
        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.sortArrayByParityII([4,2,5,7]))