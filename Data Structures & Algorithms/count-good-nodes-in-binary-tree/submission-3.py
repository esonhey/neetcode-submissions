# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, m):
            nonlocal count
            if root:
                if root.val >= m:
                    count += 1
                dfs(root.left, max(root.val, m))
                dfs(root.right, max(root.val, m))
        dfs(root, root.val)
        return count

        