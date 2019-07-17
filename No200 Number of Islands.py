class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.infect(grid, i, j, m, n)
                    print(grid)
                else:
                    continue
        return count

    def infect(self, grid, i, j, m, n):
        if i >= m or j >= n or grid[i][j] != "1" or i < 0 or j < 0:
            return
        grid[i][j] = "2"
        self.infect(grid, i+1, j, m, n)
        self.infect(grid, i-1, j, m, n)
        self.infect(grid, i, j+1, m, n)
        self.infect(grid, i, j-1, m, n)

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.numIslands(
[["1","0","1","1","0","1","1"]]))