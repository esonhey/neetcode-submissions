class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums: number[]): number {
        return nums.reduce((acc, num) => acc ^ num, 0)
    }
}
