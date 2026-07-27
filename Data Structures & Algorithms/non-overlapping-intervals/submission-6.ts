class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    hasOverlap(int1: number[], int2: number[]) {
        if (int2[0] < int1[1]) return true
        return false
    }
    eraseOverlapIntervals(intervals: number[][]): number {
        let sorted = [...intervals.map(x => [...x])].sort((a, b)=> {
            if (a[0] === b[0]) return a[1] - b[1]
            return a[0] - b[0]
        })
        console.log(sorted)
        for (let i=0; i < sorted.length -1;) {
            if (this.hasOverlap(sorted[i], sorted[i+1])) {
                if (sorted[i+1][1] < sorted [i][1]) {
                    sorted.splice(i, 1)
                } else {
                    sorted.splice(i+1, 1)
                }
            } else {
                i++
            }

        }
        return intervals.length - sorted.length
    }
}
