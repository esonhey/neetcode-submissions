# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dif(root):
            nonlocal balanced

            if not root: return 0

            l = dif(root.left)
            r = dif(root.right)

            balanced = balanced and (abs(l - r) <= 1)
            return max(l, r) + 1
        
        dif(root)

        return balanced