'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        distinct = 0
        def nQueen(row):
            nonlocal distinct
            if row == n:
                distinct += 1
                return distinct
            for column in range(0, n):
                if isSafe(board, row, column, n):
                    board[row][column] = 'Q'
                    nQueen(row + 1)
                    board[row][column] = '.'
                    
        def isSafe(board, r, c, n):
            # check vertical and horizontal lines
            for i in range(n):
                if board[i][c] == 'Q' or board[r][i] == 'Q':
                    return False
            
            # check left up and right up diagonally
            for i in range(1, n):
                if r - i >= 0 and c - i >= 0:
                    if board[r - i][c - i] == 'Q':
                        return False
                if r - i >= 0 and c + i < n:
                    if board[r - i][c + i] == 'Q':
                        return False
            return True
        nQueen(0)
        return distinct
    
mySol = Solution()
n = 4
print(mySol.solveNQueens(n))