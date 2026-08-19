class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack = []
        for (const c of s) {
            if (c === '(' || c === '[' || c === '{') {
                stack.push(c)
                continue
            }
            const last = stack.pop()
            if (c === ']' && last !== '[') return false
            if (c === ')' && last !== '(') return false
            if (c === '}' && last !== '{') return false
        }
        return !stack.length
    }
}
