'''You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.'''

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        deleted = 0
        m = len(grid)                   # number of rows
        n = len(grid[0])                # number of columns
        for i in range(0, n):           # loop over the number of columns
            maxx = []                   # initialise the list to store maximum number deleted in each row
            for j in range(0, m):       # loop over the number of rows
                x = max(grid[j])        # calculate the max element in each row
                maxx.append(x)          # add each max element to the list
                grid[j].remove(x)       # remove the max element from each row
            y = max(maxx)               # calculate max element from the maxx list
            deleted += y                # add it to the deleted list
        return deleted                  # return deleted list

mySol = Solution()
grid = [[1,2,4],
        [3,3,1]]
print(mySol.deleteGreatestValue(grid))