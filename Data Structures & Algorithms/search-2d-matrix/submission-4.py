class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        s, e = 0, m * n - 1
        while s <= e:
            i = e - s // 2
            x, y = i // n, i % n
            curr = matrix[x][y]
            if curr == target:
                return True
            if curr < target:
                s = i+1
            else:
                e = i-1
        return False