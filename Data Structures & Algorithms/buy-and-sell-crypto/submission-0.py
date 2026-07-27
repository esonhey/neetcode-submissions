class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = prices[0]
        maxDif = 0
        for p in prices:
            print(p, '-', mini, ':', maxi)
            if p < mini:
                mini = p
                maxi = p
            elif p > maxi:
                maxi = p
                maxDif = max(maxi - mini, maxDif)
        return maxDif
    
