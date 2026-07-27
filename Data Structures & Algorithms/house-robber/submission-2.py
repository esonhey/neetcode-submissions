class Solution:
    def rob(self, nums: List[int]) -> int:
        maxIdx = len(nums) - 1
        mem = {}
        def dfs(idx):
            if idx in mem:
                return mem[idx]

            if idx > maxIdx: 
                return 0
            
            mem[idx] = max(nums[idx]+ dfs(idx + 2), dfs(idx + 1))
            return mem[idx]
        
        return dfs(0)