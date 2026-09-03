class Solution {
    /**
     * @param {number[]} digits
     * @return {number[]}
     */
    plusOne(digits: number[]): number[] {
        let carry = 1
        let i = digits.length - 1
        while (i >= 0 && carry) {
            const sum = digits[i] + carry
            if (sum > 9) {
                digits[i] = 0
                carry = 1
            } else {
                digits[i] = sum
                carry = 0
            }
            i--
        }
        if (carry === 1) {
            digits.unshift(1)
        }
        return digits
    }
}
