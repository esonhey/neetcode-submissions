class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        lastIdx = len(cost) - 1
        def dp(idx):
            if idx > lastIdx:
                return 0

            if idx in mem:
                return mem[idx]


            val = cost[idx] + min(dp(idx+1), dp(idx+2))
            mem[idx] = val
            print(mem)
            return val

        return min(dp(0), dp(1))
        