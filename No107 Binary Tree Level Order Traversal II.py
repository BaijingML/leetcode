# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root.val == None:
            return []
        else:
            queue = []
            queue.append(root)
            result = []
            while queue:
                temp_result = []
                for i in queue:
                    if i.left != None:
                        queue.append(i.left)
                    if i.right != None:
                        queue.append(i.right)
                    temp_result.append(i.val)
                result.append(temp_result)
        return result