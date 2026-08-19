class Solution {
    add = (a, b) => a + b
    sub = (a, b) => a - b
    mul = (a, b) => a * b
    div = (a, b) => Math.trunc(a / b)

    operands = {
        '+': this.add,
        '-': this.sub,
        '*': this.mul,
        '/': this.div
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
