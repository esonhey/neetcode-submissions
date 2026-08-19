class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    charMap = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    isValid(s: string): boolean {
        const stack = []
        for (const c of s) {
            if (c === '(' || c === '[' || c === '{') {
                stack.push(c)
                continue
            }
            if (stack.pop() !== this.charMap[c]) return false
        }
        return !stack.length
    }
}
