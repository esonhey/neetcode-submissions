class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        square = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]] 
        for i in range(len(board)):
            for j in range(len(board[0])):
                v = board[i][j]
                if v == '.':
                    continue
                r = rows[i]
                c = cols[j]
                s = square[i//3][j//3]
                if v in r or v in c or v in s:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                square[i//3][j//3].add(v)
        return True