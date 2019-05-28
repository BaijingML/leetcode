class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [grid[0][0]]
        for i in range(1, n):
            result.append(grid[0][i]+result[-1])
        print(result)
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    result[j] = min(result[j-1], result[j]) + grid[i][j]
                else:
                    result[j] += grid[i][j]
        return result[-1]