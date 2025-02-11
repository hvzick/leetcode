'''Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.'''

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(0, m):           # loop through rows
            for j in range(0, n):       # loop through columns
                if grid[i][j] < 0:      # check if number a current index is less than 0
                    count += 1          # increment the count
        return count

mySol = Solution()
grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
print(mySol.countNegatives(grid))