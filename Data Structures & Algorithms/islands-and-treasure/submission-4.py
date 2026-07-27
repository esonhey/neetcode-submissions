class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(x, y, acc, visited, who):
            visited.add((x, y))
            n = grid[x][y]
            if n == -1: return
            if acc < n:
                grid[x][y] = acc
                for i, j in filter(
                    lambda x: x[0]>=0 and x[0]< len(grid) and x[1] >= 0 and x[1]<len(grid[0]) and (x[0], x[1]) not in visited, 
                    [(x, y-1), (x, y+1),(x+1, y), (x-1, y)]):
                    new_vis = set(visited)
                    dfs(i, j, acc+1, new_vis, (x, y))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                n = grid[i][j]
                if n == 0:
                    for x, y in filter(
                        lambda x: x[0]>=0 and x[0]< len(grid) and x[1] >= 0 and x[1]<len(grid[0]), 
                        [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):
                        dfs(x, y, 1, set([(i, j)]), (i, j))
