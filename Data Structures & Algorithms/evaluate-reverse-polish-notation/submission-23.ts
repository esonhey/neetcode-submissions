class Solution {
    add = (a, b) => a + b
    sub = (a, b) => b - a
    mul = (a, b) => a * b
    div = (a, b) => Math.trunc(b / a)

    o= {
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
            if ('+-*/'.includes(c)) {
                s.push(this.o[c](s.pop(), s.pop()))
            } else {
                s.push(parseInt(c))
            }
        })
        return s[0]
    }
}
