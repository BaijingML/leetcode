class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                result[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                result[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]