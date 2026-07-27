# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, node: Optional[ListNode], visited = None) -> bool:
        if not visited: visited = set([])
        if not node: return False
        if node in visited: return True
        visited.add(node)
        return self.hasCycle(node.next, visited)