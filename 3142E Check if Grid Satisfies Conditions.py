'''You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false.'''

class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if j == n-1 and i == m-1:                                           # for last element
                    pass
                elif j == n-1:
                    if grid[i][j] != grid[i+1][j]:                                  # for last column
                        return False
                elif i == m-1:
                    if grid[i][j] == grid[i][j+1]:                                  # for last row
                        return False
                else:
                    if grid[i][j] == grid[i][j+1] or grid[i][j] != grid[i+1][j]:    # for all other elements
                        return False
        return True

mySol = Solution()
grid = [[1,0,2],
        [1,0,2]]
print(mySol.satisfiesConditions(grid))