# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        index_of_inorder = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:index_of_inorder+1], inorder[:index_of_inorder])
        right = self.buildTree(preorder[index_of_inorder+1:], inorder[index_of_inorder+1:])
        return TreeNode(preorder[0], left, right)
        