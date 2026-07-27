/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        const dummy = new ListNode(0, head)
        let left = dummy
        let right = head
        let activeIdx = 0
        while (activeIdx < n) {
            right = right.next
            activeIdx += 1
        }
        while (right){
            right = right.next
            left = left.next
        }
        left.next = left.next.next
        return dummy.next
        
    }
}
