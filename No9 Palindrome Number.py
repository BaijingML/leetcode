#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 20:52
@File    : No9 Palindrome Number
@Software: PyCharm
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        left, right = 0, len(m) - 1
        while left < right:
            if m[left] == m[right]:
                left += 1
                right -= 1
            else:
                return False
        return True