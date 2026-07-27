class GridGraph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.graph = self.build_graph()

    def get_neighbors(self, row, col):
        """Returns valid neighbors (up, down, left, right)."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row_delta, col_delta)
        neighbors = []

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] <= self.grid[row][col]:
                neighbors.append((r, c))
        return neighbors

    def build_graph(self):
        graph = {}
        for row in range(self.rows):
            for col in range(self.cols):
                graph[(row, col)] = self.get_neighbors(row, col)
        return graph


class Solution:
    def __init__(self):
        self.pacific = set()
        self.atlantic = set()

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    self.pacific.add((i, j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    self.atlantic.add((i, j))

        grid_graph = GridGraph(heights)

        def check_path_to_atlantic(row, col, visited = set()):
            if visited is None:
                visited = set()

            if (row, col) in self.atlantic:
                return True

            if (row, col) in visited:
                return False
            visited.add((row, col))

            for [ar, ac] in grid_graph.graph.get((row, col), []):
                if check_path_to_atlantic(ar, ac):
                    self.atlantic.add((row, col))
                    return True
            return False
        
        def check_path_to_pacific(row, col, visited = set()):
            if visited is None:
                visited = set()
                
            if (row, col) in self.pacific:
                return True

            if (row, col) in visited:
                return False
            visited.add((row, col))

            for [ar, ac] in grid_graph.graph.get((row, col), []):
                if check_path_to_pacific(ar, ac):
                    self.pacific.add((row, col))
                    return True
            return False

        for i in range(len(heights[0])):
            for j in range(len(heights)):
                check_path_to_atlantic(j, i)
                check_path_to_pacific(j, i)

                
        # print(grid_graph.graph)
        # print(grid_graph.get_neighbors())
        return list(self.pacific.intersection(self.atlantic))
        