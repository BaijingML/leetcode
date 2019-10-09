#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/8 20:08
@File    : No1079 Letter Tile Possibilities
@Software: PyCharm
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ""
        left_count = 0
        for i in S:
            if i == "(":
                left_count += 1
                stack.append(i)
            else:
                left_count -= 1
                stack.append(i)
                if left_count == 0:
                    result += ''.join(stack[1:-1])
                    stack = []
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.removeOuterParentheses("()()"))