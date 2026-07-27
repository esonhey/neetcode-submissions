class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    searchRange(nums: number[], target: number): number[] {
        const start = nums.findIndex(x => x === target);
        if (start === -1) return [-1, -1]
        let end = start + 1
        while (end < nums.length && nums[end] === target) {
            end += 1
        }
        return [start, end -1]
    }
}
