class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxDif = 0
        for p in prices:
            if p < mini:
                mini = p
            maxDif = max(p - mini, maxDif)
        return maxDif
    
