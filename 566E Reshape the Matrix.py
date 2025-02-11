'''In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.'''

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        if (m * n) != (r * c):            # check if it is possible to reshape the matrix
            return mat                    # if not return the original matrix
        temp = []                         # initialise a temporary list
        for i in range(0, m):             
            for j in range(0, n):
                temp.append(mat[i][j])    # store all the values of original matrix
        matrix = []                       # initialise the new reshaped matrix
        k = 0                             # initialise a variable for temp list index
        for i in range(0, r):
            x = []                        # temporary matrix to store new columns
            for j in range(0, c):
                x.append(temp[k])         # add elements from temp to this matrix
                k += 1
            matrix.append(x)              # add rows to the new matrix
        return matrix

mySol = Solution()
matrix = [  [1,2],
            [3,4],  ]
r = 2
c = 4
print(mySol.matrixReshape(matrix, r, c))