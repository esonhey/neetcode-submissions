class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let min = prices[0]
        for (let i = 0; i < prices.length; i++){
            max = Math.max(prices[i] - min, max)
            min = Math.min(prices[i], min)
        }
        return max
    }
}
