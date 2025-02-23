'''Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament.'''

class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        n = len(grid)
        for i in range(0, n):               # loop over each row
            if grid[i].count(1) == n-1:     # check if the count of 1 in current row is equal to n-1 thats the champion row because thats won over all rows
                return i                    # return that row

mySol = Solution()
grid = [[0,0,1],
        [1,0,1],
        [0,0,0]]
print(mySol.findChampion(grid))