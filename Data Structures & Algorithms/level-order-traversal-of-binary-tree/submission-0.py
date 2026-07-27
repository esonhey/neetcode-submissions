# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, l):
            nonlocal res
            if not node: return
            if l >= len(res):
                res.append([node.val])
            else:
                res[l].append(node.val)
            dfs(node.left, l+1)
            dfs(node.right, l+1)
        dfs(root, 0)
        return res
        