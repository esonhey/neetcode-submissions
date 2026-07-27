# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        def dfs(node):
            if node.val in visited:
                return True
            visited.add(node.val)
            if not node.next:
                return False
            return dfs(node.next)

        return dfs(head)