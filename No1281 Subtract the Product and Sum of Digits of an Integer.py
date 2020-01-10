#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2020/1/10 19:46
@File    : No1281 Subtract the Product and Sum of Digits of an Integer
@Software: PyCharm
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        sum, product = 0, 1
        for i in range(len(n_str)):
            product *= int(n_str[i])
            sum += int(n_str[i])
        return product - sum

if __name__ == '__main__':
    solu = Solution()
    print(solu.subtractProductAndSum(4421))