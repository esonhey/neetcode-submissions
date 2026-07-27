class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let l = 0;
        let r = 1;
        while (r < prices.length){
            max = Math.max(prices[r] - prices[l], max)
            if (prices[r] <= prices[l]) {
                l = r
            }
            r++
        }
        return max
    }
}
