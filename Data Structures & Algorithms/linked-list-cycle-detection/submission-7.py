# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode], visited = None) -> bool:
        if not visited: visited = set([])
        if not head: return False
        if head in visited: return True
        visited.add(head)
        return self.hasCycle(head.next, visited)