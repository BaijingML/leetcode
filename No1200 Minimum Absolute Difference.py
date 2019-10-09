#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 19:05
@File    : No1200 Minimum Absolute Difference
@Software: PyCharm
"""
class Solution:
    def minimumAbsDifference(self, arr):
         arr.sort()
         result = [[arr[0], arr[1]]]
         min_diff = arr[1] - arr[0]
         for i in range(2, len(arr)):
            if arr[i] - arr[i-1] > min_diff:
                continue
            elif arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
            else:
                min_diff = arr[i] - arr[i-1]
                result = [[arr[i-1], arr[i]]]
         return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumAbsDifference([40,11,26,27,-20]))