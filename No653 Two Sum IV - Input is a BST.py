# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        value = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop(-1)
                value.append(node.val)
                root = node.right
        small = 0
        big = len(value) - 1
        while small < big:
            if value[small] + value[big] == k:
                return True
            elif value[small] + value[big] > k:
                big -= 1
            else:
                small += 1
        return False
