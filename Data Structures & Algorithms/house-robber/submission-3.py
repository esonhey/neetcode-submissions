class Solution:
    def rob_dynamic_top_down(self, nums: List[int]) -> int:
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

    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for rob in nums:
            temp = max(rob1 + rob, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2