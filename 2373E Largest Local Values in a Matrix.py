'''You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.'''
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = []                         # initialise an empty matrix
        for i in range(n-2):                  
            x = []                            # initialise another empty matrix
            for j in range(n-2):              # this matrix should be (n-2) x (n-2)
                x.append(0)                   # fill the inner matrix with zeroes
            maxLocal.append(x)                # append the inner matrix to outer matrix
        for i in range(1, n-1):               # exclude outer columns
            for j in range(1, n-1):           # exclude outer rows
                m = max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                        grid[i][j-1], grid[i][j], grid[i][j+1],
                        grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                        )                     # check max of the 3x3 matrix
                maxLocal[i-1][j-1] = m        # add it to the new matrix
        return maxLocal

mySol = Solution()
grid1 = [[9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]
grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(mySol.largestLocal(grid1))
print(mySol.largestLocal(grid2))