'''Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.

Return the matrix answer.'''

class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        no1 = []
        m = len(matrix)                         # lenght of rows 
        n = len(matrix[0])                      # length for columns 
        for i in range(0, n):                   # transpose the matrix
            no2 = []
            for j in range(0, m):
                no2.append(matrix[j][i])
            no1.append(no2)
        answer = matrix.copy()
        for i in range(0, m):
            for j in range(0, n):
                if answer[i][j] == -1:          # check if current value is -1
                    x = max(no1[j])             # calculate max of a column 
                    answer[i][j] = x            # replace -1 with the max value of the column         
        return answer

# SOLVED IN LESS THAN 5 MINUTES

mySol = Solution()
matrix = [  [1,2,-1],
            [4,-1,6],
            [7,8,9]  ]
gfd = [ [1, 4, 7], 
        [2, -1, 8], 
        [-1, 6, 9] ]
print(mySol.modifiedMatrix(matrix))