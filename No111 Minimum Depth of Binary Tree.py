#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/15 10:13
@File    : No111 Minimum Depth of Binary Tree
@Software: PyCharm
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        count = 1
        num = 0
        depth = 1
        while stack:
            for i in range(count):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    num += 1
                if node.right:
                    stack.append(node.right)
                    num += 1
                if not node.left and not node.right:
                    return depth
            count = num
            num = 0
            depth += 1
        return depth
