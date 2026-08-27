let globalSet = new Set()
class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    isHappy(n: number): boolean {
        const cyclicSet = new Set([...globalSet])

        function cycle(n: number): number {
            return n.toString()
                .split('')
                .map(s => Number(s))
                .reduce((acc, n) => acc + (n * n), 0)
        }
        while (true) {
            if (cyclicSet.has(n)) {
                globalSet = cyclicSet
                return false
            }
            cyclicSet.add(n)
            n = cycle(n)
            if (n === 1) {
                return true 
            }

        }
    }
}
