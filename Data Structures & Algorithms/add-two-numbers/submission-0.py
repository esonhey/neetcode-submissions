# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        curr = newNode
        carry = 0
        while l1 or l2 or carry:
            sumN = 0
            if l1 and l2:
                sumN = l1.val + l2.val + carry
                n = sumN % 10
            elif l1:
                sumN = l1.val + carry
                n = sumN % 10
            elif l2:
                sumN = l2.val + carry
                n = sumN % 10
            else:
                n = 1
            carry = 1 if sumN > 9 else 0
            curr.next = ListNode(n)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return newNode.next

        