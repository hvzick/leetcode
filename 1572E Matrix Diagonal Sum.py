'''Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal
and all the elements on the secondary diagonal that are not part
of the primary diagonal.
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.'''

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        m_sum = 0                                       # initialise the sum variable
        n = len(mat)                                    # length of matrix
        for i in range(0, len(mat)):                    # iterates over columns
            for j in range(0, len(mat[i])):             # iterates of rows
                if i == j:                              # checks for primary diagonal
                    m_sum += mat[i][j]                  # adds values of primary diagonal
            m_sum += mat[i][n-1-i]                      # adds values of secondary diagonal
        if n % 2 != 0:                                  # checks if the matrix has odd values
            x = n // 2                                  # calculates mid value
            m_sum -= mat[x][x]                          # subtracts mid value because it was calculated twice
        return m_sum                

mySol = Solution()
matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9]  
            ]
mat = [ [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]  
        ]
print(mySol.diagonalSum(matrix))
print(mySol.diagonalSum(mat))