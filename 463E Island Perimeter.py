'''You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
'''

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        n = len(grid[0])
        m = len(grid) 
        if len(grid[0]) == 1 and len(grid) == 1:        # if there is only one element in the matrix
            return 4
        if len(grid) == 1:                              # if there is only one row in the matrix
            for i in range(0, n):
                if grid[0][i] == 1:
                    if i == 0:                          # for first column
                        perimeter += 3
                        if grid[0][i+1] == 0:   
                            perimeter += 1
                    elif i == n-1:                      # for columns in between top  and bottom left corner
                        perimeter += 3
                        if grid[0][i-1] == 0:
                            perimeter += 1
                    elif 0 < i < n-1:                    # for last column
                        perimeter += 2
                        if grid[0][i-1] == 0:
                            perimeter += 1
                        if grid[0][i+1] == 0:
                            perimeter += 1
        else:                                           # when there are multiple rows in the matrix
            for i in range(0, m):
                for j in range(0, n):
                    if len(grid[i]) == 1:               # when a row has only one element
                            if grid[i][j] == 1:           
                                if i == 0:              # for first row
                                    perimeter += 3
                                    if grid[i+1][0] == 0:   
                                        perimeter += 1
                                elif i == m-1:          # for rows in between top  and bottom left corner
                                    perimeter += 3
                                    if grid[i-1][0] == 0:
                                        perimeter += 1
                                elif 0 < i < m-1:       # for last row
                                    perimeter += 2
                                    if grid[i-1][0] == 0:
                                        perimeter += 1
                                    if grid[i+1][0] == 0:
                                        perimeter += 1
                    else:                               # when a row has multiple elements
                        if grid[i][j] == 1:             # for top left corner
                            if i == 0 and j == 0:
                                perimeter += 2
                                if grid[i][j+1] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                            elif i == 0 and j == n-1:    # for top right corner
                                perimeter += 2
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                            elif i == 0 and 0 < j < n-1: # for first column in between top left and right corner
                                perimeter += 1
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                                if grid[i][j+1] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                            elif 0 < i < m-1 and j == 0: # for first column in between top and bottom left corner
                                perimeter += 1
                                if grid[i][j+1] == 0:
                                    perimeter += 1
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                            elif 0 < i < m-1 and j == n-1: # for last column in between top and bottom right corner
                                perimeter += 1
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                            elif 0 < i < m-1 and 0 < j < n-1:  # for elements in between all four corners
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                                if grid[i+1][j] == 0:
                                    perimeter += 1
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                                if grid[i][j+1] == 0:
                                    perimeter += 1
                            elif i == m-1 and j == 0: # for bottom left corner
                                perimeter += 2
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                                if grid[i][j+1] == 0:
                                    perimeter += 1
                            elif i == m-1 and j == n-1:# for bottom right corner
                                perimeter += 2
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                            elif i == m-1 and 0 < j < n-1: # for last column in between bottom left and right corner
                                perimeter += 1
                                if grid[i-1][j] == 0:
                                    perimeter += 1
                                if grid[i][j-1] == 0:
                                    perimeter += 1
                                if grid[i][j+1] == 0:
                                    perimeter += 1
        return perimeter

mySol = Solution()
grid1 = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
grid2 = [[1],[0]]
grid3 = [[1]]
grid4 = [[1],[1]]
grid5 = [[1,1]]
# print(mySol.islandPerimeter(grid1))
# print(mySol.islandPerimeter(grid2))
# print(mySol.islandPerimeter(grid3))
# print(mySol.islandPerimeter(grid4))
print(mySol.islandPerimeter(grid5))