class Solution {
    add = (a, b) => a + b
    sub = (a, b) => b - a
    mul = (a, b) => a * b
    div = (a, b) => Math.trunc(b / a)

    o = {
        '+': this.add,
        '-': this.sub,
        '*': this.mul,
        '/': this.div
    }

    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(t: string[]): number {
        const s= []
        t.forEach(c => {
            s.push('+-*/'.includes(c) ? this.o[c](s.pop(), s.pop()): parseInt(c))
        })
        return s[0]
    }
}
