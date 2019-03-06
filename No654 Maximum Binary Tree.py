# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            # if len(nums) == 1:
            #     return TreeNode(nums[0])
            num_max_index = 0
            num_max = nums[0]
            for i in range(len(nums)):
                if nums[i] > num_max:
                    num_max = nums[i]
                    num_max_index = i
                else:
                    continue
            root = TreeNode(num_max)
            root.left = self.constructMaximumBinaryTree(nums[:num_max_index])
            root.right = self.constructMaximumBinaryTree(nums[num_max_index+1:])
            return root
        else:
            return None