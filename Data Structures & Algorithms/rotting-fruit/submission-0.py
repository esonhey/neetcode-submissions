from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = deque()
        fresh = set()
        steps = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rottens.append((i, j, 0))
        while rottens:
            r = rottens.popleft()
            steps = max(steps, r[2])
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for x, y in dirs:
                xx = r[0] + x
                yy = r[1] + y
                if (xx, yy) in fresh:
                    fresh.remove((xx, yy))
                    rottens.append((xx, yy, r[2]+1))
                

        return steps if not fresh else -1