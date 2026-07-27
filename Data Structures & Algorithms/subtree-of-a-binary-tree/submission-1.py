# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], x = "m") -> bool:
        def dfs(root, subRoot):
            if not subRoot and not root: return True
            if not root or not subRoot: return False

            if root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            return False
        
        if not subRoot: return True
        if not root: return False

        if root.val == subRoot.val and dfs(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot, "l") or self.isSubtree(root.right, subRoot, "r")

                    
        