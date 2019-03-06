"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        result = []
        if root == None:
            return result
        stack = [root]
        while stack:
            temp = []
            next_stack = []     # 创建新的stack替换旧的，保证里面都是一个层级的节点
            for node in stack:
                temp.append(node.val)
                for child in node.children:
                    next_stack.append(child)
            result.append(temp)
            stack = next_stack
        return result
