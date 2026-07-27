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
                if (v in rows[i] 
                    or v in cols[j] 
                    or v in square[i//3][j//3]):
                    return False
                rows[i].add(v)
                cols[j].add(v)
                square[i//3][j//3].add(v)
        return True