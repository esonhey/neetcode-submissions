class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const prefix = Array.from({ length: nums.length }, () => 1)
        const suffix = Array.from({ length: nums.length }, () => 1)
        for (let i=1; i<nums.length; i++) {
            prefix[i] = prefix[i-1] * nums[i-1]
        }
        for (let i=nums.length-2; i>=0; i--) {
            suffix[i] = suffix[i+1] * nums[i+1]
        }
        const result = []
        for (let i=0; i<nums.length; i++) {
            result.push(suffix[i] * prefix[i])
        }
        return result
    }
}


