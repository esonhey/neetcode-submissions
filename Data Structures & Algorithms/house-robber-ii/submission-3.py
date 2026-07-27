class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        mem = {False: {}, True: {}}
        def dfs(start, notEnd):
            end = len(nums) - 1 - (1 if notEnd else 0)
            if start in mem[notEnd]:
                return mem[notEnd][start]

            if start > end:
                return 0

            mem[notEnd][start] = max(nums[start] + dfs(start + 2, notEnd), dfs(start + 1, notEnd))
            return mem[notEnd][start]
        
        return max(dfs(0, True), dfs(1, False))

            

        