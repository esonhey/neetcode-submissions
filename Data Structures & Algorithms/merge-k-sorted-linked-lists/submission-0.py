# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myList = ListNode()

        refToList = myList

        while len(lists) > 1:
            nextNode = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[nextNode].val:
                    nextNode = i

            nextNodeValue = lists[nextNode].val

            lists[nextNode] = lists[nextNode].next
            if lists[nextNode] == None:
                lists = [x for x in lists if x != None]

            myList.next = ListNode(nextNodeValue)
            myList = myList.next
        
        if len(lists) == 1:
            myList.next = lists[0]

        return refToList.next

        