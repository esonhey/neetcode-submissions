class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hashMap = new Map()
        for (let i=0; i <= nums.length; i++) {
            const complementIdx = hashMap.get(nums[i]) 
            if (complementIdx !== undefined) return [complementIdx, i]

            hashMap.set(target - nums[i], i)
        }
        return []
    }
}
