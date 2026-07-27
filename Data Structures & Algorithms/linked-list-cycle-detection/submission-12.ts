//  class ListNode {
//     constructor(val = 0, next = null) {
//         this.val = val;
//         this.next = next;
//     }
//  }

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head: ListNode | null): boolean {
        if (!head) return false
        let slow = head.next
        if (!slow) return false
        let fast = slow.next
        while (fast) {
            if (fast === slow) return true
            fast = fast.next
            if (fast) fast = fast.next

            slow = slow.next
        }
        return false
    }
    hasCycle1(head: ListNode | null): boolean {
        const visited = new Set()
        while (head) {
            if (visited.has(head)) {
                return true
            }
            visited.add(head)
            head = head.next
        }
        return false
    }
}
