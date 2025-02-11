'''A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.'''

class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        for i in range(0, n):
            for j in range(0, n):
                if i == j or i == n - 1 - j:    # check diagonals
                    if grid[i][j] == 0:         # check if diagonal elements are equal to 0
                        return False            # return False
                else:                           # for non diagonal elements
                    if grid[i][j] != 0:         # check if they are not equal to 0
                        return False            # return False
        return True

mySol = Solution()
grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
print(mySol.checkXMatrix(grid))