class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let l = 0
        let r = numbers.length - 1

        while (l < r) {
            const left = numbers[l]
            const right = numbers[r]
            const sum = left + right

            if (sum === target) return [l+1, r+1]
            if (sum < target) {
                l++
            } else {
                r--
            }
        }
    }
}
