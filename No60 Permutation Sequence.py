#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 21:42
@File    : No60 Permutation Sequence
@Software: PyCharm
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = [1]
        result = ""
        d = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1, n+1):
            temp.append(i * temp[i-1])
        k -= 1
        for i in range(n, 0, -1):
            j = int((k) / temp[i-1])
            k = k % temp[i-1]
            result += d[j]
            d.remove(d[j])
        return result
        
if __name__ == '__main__':
    solu = Solution()
    print(solu.getPermutation(4, 9))