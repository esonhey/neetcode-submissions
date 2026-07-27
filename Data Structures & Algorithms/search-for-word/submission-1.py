class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bruteForceRec(word, visited, position):
            if not word:
                return True
            x, y = position
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (i >= 0 and i < len(board)) and (j >= 0 and j < len(board[0])) and (i, j) not in visited and board[i][j] == word[0]:
                    x = bruteForceRec(word[1:], visited | {(i, j)}, (i, j))
                    if x:
                        return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    x = bruteForceRec(word[1:], set([(i, j)]), (i, j))
                    if x:
                        return True
        return False

        