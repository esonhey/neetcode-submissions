class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        square = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        for i in range(len(board)):
            for j in range(len(board[0])):
                v = board[i][j]
                if v == '.':
                    continue
                r = rows[i]
                c = cols[j]
                square_pos = int(i / 3) + int(j/3) * 3
                s = square[square_pos]
                if v in r or v in c or v in s:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                square[square_pos].add(v)
        return True