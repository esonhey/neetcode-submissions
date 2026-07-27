class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        pos = 0
        while pos <= maxIdx and pos < len(nums):
            maxIdx = max(maxIdx, pos + nums[pos])
            pos += 1
        return maxIdx >= len(nums) - 1
        