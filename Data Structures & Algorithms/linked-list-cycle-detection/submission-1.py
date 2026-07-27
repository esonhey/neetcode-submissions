# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        def dfs(node):
            if not node: return False

            if node.val in visited:
                return True
                
            visited.add(node.val)

            return dfs(node.next)

        return dfs(head)