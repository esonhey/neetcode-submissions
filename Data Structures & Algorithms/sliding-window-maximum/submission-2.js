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
            while (deque.length > 0 && deque[0] < i - k + 1) {
                deque.shift()
            }
        
            while (deque.length > 0 && nums[deque[deque.length - 1]] <= nums[i]) {
                deque.pop()
            }
        
            deque.push(i)
        
            if (i >= k - 1) {
                result.push(nums[deque[0]])
            }
        }
    
        return result 
    }
}
