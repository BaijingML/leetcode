# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def search(node):
            if node.left:
                search(node.left)
            result.append(node.val)
            if node.right:
                search(node.right)

        if not root:
            return []
        result = []
        if root.left:
            search(root.left)
        result.append(root.val)
        if root.right:
            search(root.right)
        return result

    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 非递归遍历
        result = []
        temp = []
        while temp or root:
            while root:
                temp.append(root)
                root = root.left
            if temp:
                node = temp.pop(-1)
                result.append(node.val)
                root = node.right
        return result
