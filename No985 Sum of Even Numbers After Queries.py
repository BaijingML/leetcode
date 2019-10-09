#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 16:52
@File    : No985 Sum of Even Numbers After Queries
@Software: PyCharm
"""
class Solution:
    def sumEvenAfterQueries(self, A, queries):
        temp = 0
        result = []
        for i in A:
            if i % 2 == 0:
                temp += i
        for value, index in queries:
            pre_value = A[index]
            A[index] += value
            if pre_value % 2 == 0:
                temp -= pre_value
            if A[index] % 2 == 0:
                temp += A[index]
            result.append(temp)
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))