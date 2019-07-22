# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        stack = [root]
        temp = []
        num = 1
        while num:
            for i in range(num):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                temp.append(node.val)
                # print(temp, stack)
            num = len(stack)
            result.append(sum(temp) / len(temp))
            temp = []
        return result
