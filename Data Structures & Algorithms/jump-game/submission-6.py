class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(nums):
            if len(nums) <= 1:
                return True
            
            if nums[0] >= len(nums) - 1:
                return True

            canReach = False

            for i in range(nums[0], 0, -1):
                if dfs(nums[i:]):
                    return True
            return False
        return dfs(nums)

        