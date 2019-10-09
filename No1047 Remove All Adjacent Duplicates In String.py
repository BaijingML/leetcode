#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/3 23:07
@File    : No1047 Remove All Adjacent Duplicates In String
@Software: PyCharm
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if stack and stack[-1] == i:
                stack.pop(-1)
            else:
                stack.append(i)

        return "".join(stack)


if __name__ == '__main__':
    solu = Solution()
    print(solu.removeDuplicates("aaaaaaaa"))