#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2020/1/10 20:10
@File    : No1221 Split a String in Balanced Strings
@Software: PyCharm
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, left = 0, 0
        for i in s:
            if i == "L":
                left += 1
            else:
                left -= 1
            if left == 0:
                res += 1
        return res

if __name__ == '__main__':
    solu = Solution()
    print(solu.balancedStringSplit("RLRRRLLRLL"))