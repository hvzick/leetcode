'''You are given a n x n 2D array self.grid containing distinct elements in the range [0, n^2 - 1].

Implement the NeighborSum class:

NeighborSum(int [][]self.grid) initializes the object.
int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top, left, right, or bottom of value in self.grid.
int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in self.grid.

Input:
["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]

[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]

Output: [null, 6, 16, 16, 4]
'''

class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        s = 0
        n = len(self.grid)
        for i in range(0, n):
            for j in range(0, n):
                if value == self.grid[i][j]:
                    if i == 0 and j == 0:                         # for element at top left corner
                        s += self.grid[0][1] + self.grid[1][0]
                        return s
                    elif i == 0 and j == n-1:                     # for element at top right corner
                        s += self.grid[0][n-2] + self.grid[1][n-1]
                        return s
                    elif i == 0 and  0 < j < n-1:                 # for element at top columns between corners
                        s += self.grid[0][j-1] + self.grid[0][j+1] + self.grid[1][j]
                        return s
                    elif 0 < i < n-1 and j == 0:                  # for element at left columns between corners
                        s += self.grid[i-1][0] + self.grid[i][1] + self.grid[i+1][0]
                        return s
                    elif i == n-1 and j == 0:                     # for element at bottom left corner
                        s += self.grid[n-2][0] + self.grid[n-1][1]
                        return s
                    elif 0 < i < n-1 and j == n-1:                # for element at right column between corners
                        s += self.grid[i-1][n-1] + self.grid[i][n-2] + self.grid[i+1][n-1]
                        return s
                    elif i == n-1 and 0 < j < n-1:                # for element at bottom columns between corners
                        s += self.grid[n-1][j-1] + self.grid[n-1][j+1] + self.grid[n-2][j]
                        return s
                    elif i == n-1 and j == n-1:                   # for element at bottom right corner
                        s += self.grid[n-1][n-2] + self.grid[n-2][n-1]
                        return s
                    elif 0 < i < n-1 and 0 < j < n-1:             # for element at inner cells 
                        s += self.grid[i-1][j] + self.grid[i][j-1] + self.grid[i+1][j] + self.grid[i][j+1]
                        return s

    def diagonalSum(self, value: int) -> int:
        s = 0
        n = len(self.grid)
        for i in range(0, n):
            for j in range(0, n):
                if value == self.grid[i][j]:  
                    if i == 0 and j == 0:                        # for element at top left corner
                        s += self.grid[1][1]
                        return s
                    elif i == 0 and j == n-1:                    # for element at top right corner
                        s += self.grid[1][n-2]
                        return s
                    elif i == 0 and  0 < j < n-1:                # for element at top columns between corners
                        s += self.grid[1][j-1] + self.grid[1][j+1]
                        return s
                    elif 0 < i < n-1 and j == 0:                 # for element at left columns between corners
                        s += self.grid[i+1][1] + self.grid[i-1][1]
                        return s
                    elif i == n-1 and j == 0:                    # for element at bottom left corner
                        s += self.grid[n-2][1]
                        return s
                    elif 0 < i < n-1 and 0 < j < n-1:            # for element at inner cells 
                        s += self.grid[i-1][j-1] + self.grid[i-1][j+1] + self.grid[i+1][j-1] + self.grid[i+1][j+1]
                        return s
                    elif 0 < i < n-1 and j == n-1:               # for element at right column between corners
                        s += self.grid[i-1][n-2] + self.grid[i+1][n-2]
                        return s
                    elif i == n-1 and 0 < j < n-1:               # for element at bottom columns between corners
                        s += self.grid[n-2][j-1] + self.grid[n-2][j+1]
                        return s
                    elif i == n-1 and j == n-1:                  # for element at bottom right corner
                        s += self.grid[n-2][n-2]
                        return s
        return value

grid = [[3,6,0],
        [8,5,1],
        [2,4,7]]
mySol = NeighborSum(grid)
print(mySol.adjacentSum(7))
# print(mySol.adjacentSum(4))
# print(mySol.diagonalSum(7))
# print(mySol.diagonalSum(8))