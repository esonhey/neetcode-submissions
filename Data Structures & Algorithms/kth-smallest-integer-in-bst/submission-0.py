# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def remove_min(node):
            nonlocal res
            l = node.left
            if not l:
                res = node.val
                node = node.right
                return node
            if l.left:
                node.left = remove_min(node.left)
                return node
            node.left = remove_min(node.left)
            return node
        while k:
            root = remove_min(root)
            k -= 1
        return res
            
            

            
            

        