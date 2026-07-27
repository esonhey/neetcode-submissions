class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
       if (k < 2) return [...nums]
    k = Math.min(k, nums.length)

    const result = []
    const deque = []   // holds indices; deque[0] is always current-window max

    for (let i = 0; i < nums.length; i++) {
        // Front prune: stale index (fell out the left edge of the window).
        // Note: a `while` is safer than `if` even though only one index can fall
        // off per step in the basic form — keeps the code robust if you later
        // batch multiple steps.
        while (deque.length > 0 && deque[0] < i - k + 1) {
            deque.shift()
        }

        // Back prune: dominated indices. Using `<=` (not `<`) means we evict
        // equal-valued back entries too — keeps the deque smaller and ensures
        // the front always points to the *most recent* max on ties.
        while (deque.length > 0 && nums[deque[deque.length - 1]] <= nums[i]) {
            deque.pop()
        }

        deque.push(i)

        // First full window starts at i = k-1; from then on, every step emits.
        if (i >= k - 1) {
            result.push(nums[deque[0]])
        }
    }

    return result 
    }
}
