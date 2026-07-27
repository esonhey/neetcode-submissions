class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word

        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]

            word_found = curr_node.pop('#', None)
            if word_found:
                res.append(word_found)

            board[r][c] = '@'
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)
            board[r][c] = char

            if not curr_node:
                parent.pop(char)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return res