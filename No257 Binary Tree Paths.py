#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 13:38
@File    : No257 Binary Tree Paths
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result
        else:
            temp = ""
            self.call(root, temp, result)
            return result

    def call(self, root, temp, result):
        if not (root.left and root.right):
            result.append(temp + str(root.val))
        if root.left:
            self.call(root.left, temp + str(root.val) + "->", result)
        if root.right:
            self.call(root.right, temp + str(root.val) + "->", result)
