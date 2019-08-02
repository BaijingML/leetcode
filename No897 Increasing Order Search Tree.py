# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        temp = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop(-1)
                temp.append(node.val)
                root = node.right
        new_root = TreeNode(temp[0])
        node = new_root
        for i in range(1, len(temp)):
            node.right = TreeNode(temp[i])
            node.left = None
            node = node.right
        return new_root
