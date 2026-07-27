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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) { 
        let cary = 0
        let dummy = new ListNode()
        let x = new ListNode()
        dummy.next = x
        while (true){
            const val = (l1?.val ?? 0) + (l2?.val ?? 0) + cary
            x.val = val % 10
            cary = Math.floor(val / 10)
            if (!(l1?.next || l2?.next || cary)){
                break
            }
            x.next = new ListNode()
            l1 = l1?.next
            l2 = l2?.next
            x = x.next
        }
        return dummy.next
    }
}
