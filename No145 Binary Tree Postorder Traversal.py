#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/15 10:02
@File    : No145 Binary Tree Postorder Traversal
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.helper(root)
        return self.result

    def helper(self, node):
        if node:
            self.helper(node.left)
            self.helper(node.right)
            self.result.append(node.val)
