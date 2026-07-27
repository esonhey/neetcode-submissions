class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs_1(n) {
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
    climbStairs(n) {
        let values = [1, 2]
        if (n<3) return values[n-1]
        
        while (n>2){
            values = [values[1], values[0]+values[1]]
            n -= 1
        }
        return values[1]
    }
}
