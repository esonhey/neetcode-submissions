class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(i, j, acc):
            if ((i, j) in visited
                or i not in range(len(grid))
                or j not in range(len(grid[0]))
                or grid[i][j] == 0): return 0
            
            visited.add((i, j))
            acc[0] += 1
            dirs = [[0,1], [0,-1], [1,0], [-1, 0]]
            for x, y in dirs:
                dfs(i+x, j+y, acc)
            return acc[0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c = dfs(i, j, [0])
                res = max(res, c)
        
        return res