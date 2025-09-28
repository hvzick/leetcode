'''
#TODO You are given an m x n integer matrix matrix with the following two properties: Each row is sorted in non-decreasing order. The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_top = 0                                                                # top row ptr
        row_bottom = len(matrix) - 1                                               # bottom row ptr
        col_left = 0                                                               # left col ptr
        col_right = len(matrix[0]) - 1                                             # right col ptr
        while row_top <= row_bottom:                                               # search candidate row
            row_mid = (row_top + row_bottom) // 2                                  # middle row
            if matrix[row_mid][col_left] <= target <= matrix[row_mid][col_right]:  # target fits in this row's range
                while col_left <= col_right:                                       # binary search in row
                    mid = (col_left + col_right) // 2                              # middle col
                    if matrix[row_mid][mid] == target:                             # target found
                        return True
                    elif matrix[row_mid][mid] > target:                            # too big -> move left
                        col_right = mid - 1                                        # shrink right
                    else:                                                          # too small -> move right
                        col_left = mid + 1                                         # advance left
            elif matrix[row_mid][col_left] > target:                               # target is above -> move bottom up
                row_bottom = row_mid - 1                                           # shrink bottom
            else:                                                                  # target is below -> move top down
                row_top = row_mid + 1                                              # advance top
        return False                                                               # target not found
# ----------------- Testing -----------------

mySol = Solution()
matrix = [ [1,3,5,7],                             
          [10,11,16,20],
          [23,30,34,60] ]
target = 6              
print(mySol.searchMatrix(matrix, target))                             
print(mySol.searchMatrix(matrix=[[1]], target=1))   