'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        no1 = []
        m = len(matrix)                         # lenght of rows 
        n = len(matrix[0])                      # length for columns 
        for i in range(0, n):                   # transpose the matrix
            no2 = []
            for j in range(0, m):
                no2.append(matrix[j][i])
            no1.append(no2)
        return no1

mySol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(mySol.transpose(matrix))