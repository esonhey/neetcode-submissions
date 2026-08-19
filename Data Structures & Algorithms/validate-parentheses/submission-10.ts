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
        const openPars = new Set(Object.values(this.charMap))
        for (const c of s) {
            if (openPars.has(c)) {
                stack.push(c)
                continue
            }
            if (stack.pop() !== this.charMap[c]) return false
        }
        return !stack.length
    }
}
