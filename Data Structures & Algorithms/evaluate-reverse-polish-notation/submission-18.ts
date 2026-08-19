class Solution {
    operands = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => Math.trunc(a / b),
    }

    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stack = []
        tokens.forEach(c => {
            if ('+-*/'.includes(c)) {
                const b = stack.pop()
                const a = stack.pop()
                stack.push(this.operands[c](a, b))
            } else {
                stack.push(parseInt(c))
            }
        })
        return stack[0]
    }
}
