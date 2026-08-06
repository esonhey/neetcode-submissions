class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        /**
         * each cell belongs to 3 sets, there shouldn't be any duplicates in each set
         * we have 9 sets for rows
         * 9 sets for columns
         * and 9 sets for 9 3*3 squares
         * we should find an identifier for each
         * we can save all in a hash-map
         */
        const hashMap = {
            'r0': new Set(),
            'r1': new Set(),
            'r2': new Set(),
            'r3': new Set(),
            'r4': new Set(),
            'r5': new Set(),
            'r6': new Set(),
            'r7': new Set(),
            'r8': new Set(),

            'c0': new Set(),
            'c1': new Set(),
            'c2': new Set(),
            'c3': new Set(),
            'c4': new Set(),
            'c5': new Set(),
            'c6': new Set(),
            'c7': new Set(),
            'c8': new Set(),

            '0-0': new Set(),
            '0-1': new Set(),
            '0-2': new Set(),
            '1-0': new Set(),
            '1-1': new Set(),
            '1-2': new Set(),
            '2-0': new Set(),
            '2-1': new Set(),
            '2-2': new Set(),
        }
        for (let r=0; r<9; r++){
            for (let c=0; c<9; c++) {
                const cell = board[r][c]
                if (cell === '.') continue;
                // row check and insert
                const rowKey = `r${r}`
                if (hashMap[rowKey].has(cell))  return false;
                hashMap[rowKey].add(cell)
                // column check and insert
                const colKey = `c${c}`
                if (hashMap[colKey].has(cell)) return false;
                hashMap[colKey].add(cell)
                // square check and insert
                const sKey = `${Math.floor(r/3)}-${Math.floor(c/3)}`
                if (hashMap[sKey].has(cell)) return false;
                hashMap[sKey].add(cell)
            }
        }

        return true
    }
}
