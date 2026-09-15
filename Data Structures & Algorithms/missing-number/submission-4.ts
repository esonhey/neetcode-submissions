class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    missingNumber(nums: number[]): number {
        let res = nums.length
        nums.forEach((num, i) => {
            res = res ^ num ^ i
        })
        return res
    }
}
