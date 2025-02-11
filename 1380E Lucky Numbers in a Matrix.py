''''Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.'''

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        re = []
        no1 = []
        m = len(matrix)                         # lenght of rows 
        n = len(matrix[0])                      # length for columns 
        for i in range(0, n):                   # transpose the matrix
            no2 = []
            for j in range(0, m):
                no2.append(matrix[j][i])
            no1.append(no2)
        # for j in range(0, n):
        #     for i in range(0, m):
        #         no1[j][i] = matrix[i][j]
        for i in range(0, m):                   
            for j in range(0, n):
                n1 = min(matrix[i])             # calculate min at ith row in original matrix
                n2 = max(no1[j])                # calculate max at jth row in transposed matrix
                if n1 == n2:                    # when both are same append them to a list
                    re.append(n1)
        return re                               # return the list
        
mySol = Solution()
matrix = [  [3,7,8],
            [9,11,13],
            [15,16,17]  ]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(mySol.luckyNumbers(matrix))