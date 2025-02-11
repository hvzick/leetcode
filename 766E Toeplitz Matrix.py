'''Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.'''

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m-1):                         # loop from first to second last row because last row will be checked with the second last row
            for j in range(0, n-1):                     # loop from 0 to secon last element because last element has no diagonal
                if matrix[i][j] != matrix[i+1][j+1]:    # check if the next element in its bottom right place is equal to it or not 
                    return False
        return True

        
mySol = Solution()
matrix = [  [1,2,3,4],
            [5,1,2,3],
            [9,5,1,2]  ]
matrix = [  [53,64,90,98,34],
            [91,53,64,90,98],
            [17,91,53,64,0]  ]
print(mySol.isToeplitzMatrix(matrix))