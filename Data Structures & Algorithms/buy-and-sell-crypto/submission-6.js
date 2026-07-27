class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let min = prices[0]
        for (let sell of prices){
            max = Math.max(sell - min, max)
            min = Math.min(sell, min)
        }
        return max
    }
}
