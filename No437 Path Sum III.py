#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/7/31 16:32
@File    : No437 Path Sum III
@Software: PyCharm
"""
class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.dsf(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.count

    def dsf(self, node, value):
        if not node:
            return 0
        if node.val == value:
            self.count += 1
        self.dsf(node.left, value - node.val)
        self.dsf(node.right, value - node.val)
