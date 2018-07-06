def islandPerimeter(grid):
    perimeter = 0
    h = len(grid)
    w = len(grid[0])
    print(h, w)
    for x in range(h):
        for y in range(w):
            if grid[x][y] == 1:
                perimeter += 4
                if x>0 and grid[x-1][y]:
                    perimeter -= 2
                if y>0 and grid[x][y-1]:
                    perimeter -= 2

    return perimeter
a = [[1,1]]
print(islandPerimeter(a))