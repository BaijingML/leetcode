# class Solution(object):
    # def surfaceArea(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     n = len(grid)
    #     area = 0
    #     for i in range(n):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 area += grid[i][j] * 4 + 2
    #             else:
    #                 continue
    #             if i > 0:
    #                 area -= min(grid[i][j], grid[i-1][j]) * 2
    #             if j > 0:
    #                 area -= min(grid[i][j], grid[i][j-1]) * 2
    #     return area
def surfaceArea(grid):
    n = len(grid)
    m = len(grid[0])
    area = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                area += grid[i][j] * 4 + 2
            else:
                continue
            if i > 0:
                area -= min(grid[i][j], grid[i - 1][j]) * 2
            if j > 0:
                area -= min(grid[i][j], grid[i][j - 1]) * 2
    return area

if __name__ == "__main__":
    N, M = input().split(" ")
    N, M = int(N), int(M)
    nums = [[0 for i in range(M)] for j in range(M)]
    for i in range(1, N + 1):
        temp = list(map(int, input().split(" ")))
        for j in range(M):
            nums[i - 1][j - 1] += temp[j]
    print(surfaceArea(nums))

# if __name__ == '__main__':
#     solu = Solution()
#     print(solu.surfaceArea([[2]]))



