'''There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.'''

class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        def checkPath(row, col, number):
            if number == n * n:
                return True
            elif 0 > row or row >= n or 0 > col or col >= n:
                return
            elif number != grid[row][col]:
                return
            # grid[row][col] = 'X'
            if checkPath(row + 2, col + 1, number + 1):
                return True
            if checkPath(row + 2, col - 1, number + 1):
                return True
            if checkPath(row - 2, col + 1, number + 1):
                return True
            if checkPath(row - 2, col - 1, number + 1):
                return True
            if checkPath(row + 1, col + 2, number + 1):
                return True
            if checkPath(row + 1, col - 2, number + 1):
                return True
            if checkPath(row - 1, col + 2, number + 1):
                return True
            if checkPath(row - 1, col - 2, number + 1):
                return True
            return False
        return checkPath(0, 0, 0)
        
mySol = Solution()
grid = [
    [0,11,16,5,20],
    [17,4,19,10,15],
    [12,1,8,21,6],
    [3,18,23,14,9],
    [24,13,2,7,22]
]
print(mySol.checkValidGrid(grid))
