class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y, z = 0, 0, 0
        L = len(grid[0])
        columns_max = [0]*L
        for i in range(len(grid)):
            y += max(grid[i])

            for j in range(L):
                if grid[i][j] != 0:
                    x += 1
                if grid[i][j] > columns_max[j]:
                    columns_max[j] = grid[i][j]
        return x+y+sum(columns_max)