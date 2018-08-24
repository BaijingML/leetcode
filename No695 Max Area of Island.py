class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def findNeighbor(grid, m, n):
            if (0 <= m < len(grid)) and (0 <= n < len(grid[0])) and grid[m][n] == 1:
                grid[m][n] = 0
                sum = 1 + findNeighbor(grid, m-1, n) + findNeighbor(grid, m, n-1) + \
                      findNeighbor(grid, m+1,n) + findNeighbor(grid, m, n+1)
                return sum
            return 0
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area = max(area, findNeighbor(grid, i, j))
        return area

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))