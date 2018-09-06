class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += grid[i][j] * 4 + 2
                else:
                    continue
                if i > 0:
                    area -= min(grid[i][j], grid[i-1][j]) * 2
                if j > 0:
                    area -= min(grid[i][j], grid[i][j-1]) * 2
        return area

if __name__ == '__main__':
    solu = Solution()
    print(solu.surfaceArea([[2]]))



