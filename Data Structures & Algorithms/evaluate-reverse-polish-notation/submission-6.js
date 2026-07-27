class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    operators = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b >= 0 ? Math.floor(a / b) : Math.ceil(a / b)
    }
    evalRPN(tokens) {
        const stack = []

        for (const token of tokens) {
            if (this.operators[token]) {
                const second = stack.pop()
                const first = stack.pop()
                const result = this.operators[token](first, second)
                console.log(result)
                stack.push(result)
            } else {
                stack.push(Number(token))
            }
        }
        return stack.pop()
    }
}
