# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], acc = None) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            head.next = acc
            return head
        return self.reverseList(head.next, ListNode(head.val, acc) )