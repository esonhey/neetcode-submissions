# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList_(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next

        l, r = 0, len(arr) - 1
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l >= r:
                break
            arr[r].next = arr[l]
            r -= 1
        arr[l].next = None
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        p1, p2 = head, head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        print('mid is', p1.val)
        secondPart = p1.next
        prev = p1.next = None

        while secondPart:
            tmp = secondPart.next
            secondPart.next = prev
            prev = secondPart
            secondPart = tmp
        

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        