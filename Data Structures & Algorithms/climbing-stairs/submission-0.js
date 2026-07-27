class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const mem = {1: 1, 2: 2}
        function helper(n) {
            if (mem[n]) return mem[n]
            const rightBranch = helper(n-2)
            const leftBranch = helper(n-1)
            mem[n] = leftBranch + rightBranch
            return mem[n]
        }
        return helper(n)
    }
}
