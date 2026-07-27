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

    for (let n=0; n < nums.length - k + 1; n++){

        let max = -Infinity
        for (let kk=0; kk < k; kk++) {
            max = Math.max(max, nums[n+kk])
        }
        result.push(max)
    }
    return result
    }
}
