class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return []
        m = len(grid)
        n = len(grid[0])
        column_max = [0] * m
        row_max = [0] * n
        for i in range(m):
            for j in range(n):
                row_max[i] = max(grid[i][j], row_max[i])
                column_max[j] = max(grid[i][j], column_max[j])
        total = 0
        for i in range(m):
            for j in range(n):
                total += min(row_max[i], column_max[j]) - grid[i][j]
        return total