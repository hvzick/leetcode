'''Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.'''

class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        c = []
        for i in range(0, m):         
            c.append(mat[i].count(1))         # add the count of 1's from each row to new list where index of row == index of the list
        return c.index(max(c)), max(c)        # return index of list where 1's are maximum and number of ones
        
mySol = Solution()
mat = [[0,0,0],[0,1,1]]
print(mySol.rowAndMaximumOnes(mat))