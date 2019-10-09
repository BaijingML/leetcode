#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 19:19
@File    : No1122 Relative Sort Array
@Software: PyCharm
"""
class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []
        left = []
        d = {}
        for i in arr1:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for j in arr2:
            result += [j] * d[j]
            d.pop(j)
        for k in d.keys():
            left += [k] * d[k]
        left.sort()
        res = result + left
        return res
if __name__ == '__main__':
    solu = Solution()
    print(solu.relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31], [2,42,38,0,43,21]))
