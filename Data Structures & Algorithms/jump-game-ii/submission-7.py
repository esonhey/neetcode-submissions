import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = dict()
        def dfs(nums, idx):
            print(idx, mem)
            if idx in mem:
                return mem[idx]

            if len(nums) == 1:
                return 0

            if nums[0] >= len(nums) - 1:
                return 1
            
            minJumps = math.inf
            minIdx = 0
            maxRange = min(nums[0], len(nums))
            for i in range(maxRange, 0, -1):
                newJumps = 1 + dfs(nums[i:], idx + i)
                if newJumps < minJumps:
                    minJumps = newJumps
                    minIdx = idx + i

            if (not minIdx in mem):
                mem[minIdx] = minJumps - 1

            return minJumps
            
        return dfs(nums, 0)
            
        