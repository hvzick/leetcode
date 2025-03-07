'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # MATRIX TRANSPOSE
        n = len(matrix)
        for i in range(0, n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
        # MATRIX REFLECTION 
        for i in range(0, n):
            for j in range(0, n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp
            print(matrix)

mySol = Solution()
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(mySol.rotate(matrix))