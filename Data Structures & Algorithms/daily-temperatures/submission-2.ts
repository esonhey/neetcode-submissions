class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(tems: number[]): number[] {
        const stack: {idx: number, val: number}[] = []
        const result = new Array(tems.length).fill(0)
        for (let i = tems.length -1; i>=0; i--) {
            while (stack.length && stack[stack.length - 1].val <= tems[i]) {
                stack.pop()
            }
            if (stack.length) {
                result[i] =  stack[stack.length-1].idx - i
            }
            stack.push({ idx: i, val: tems[i] })
        }
        return result
    }
}
