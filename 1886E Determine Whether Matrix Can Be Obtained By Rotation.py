'''Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.'''

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        for c in range(4):
            if mat == target:                                       # check on each rotation
                return True
            for i in range(0, n//2):                                # for inner elements
                for j in range(i, n-i-1):                           # for rotation of sides
                    temp = mat[i][j]                                # store value of top elements 
                    mat[i][j] = mat[n - j - 1][i]                   # Left → Top
                    mat[n - j - 1][i] = mat[n - i - 1][n - j - 1]   # Bottom → Left
                    mat[n - i - 1][n - j - 1] = mat[j][n - i - 1]   # Right → Bottom
                    mat[j][n - i - 1] = temp                        # Top → Right
        return False

mySol = Solution()

matrix = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
print(mySol.findRotation(matrix, target))