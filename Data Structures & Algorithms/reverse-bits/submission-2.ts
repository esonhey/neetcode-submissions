class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n: number): number {
        let rev = 0
        for (let i = 0; i < 32; i++) {
            rev += Math.pow(2, 31-i) * (n & 1)
            n = n >> 1
        }
        return rev
    }
}
