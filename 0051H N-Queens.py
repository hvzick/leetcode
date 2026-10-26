'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

'''

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def nQueen(row):
            if row == n:
                return ans.append([''.join(r) for r in board])
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
        return ans
    
mySol = Solution()
n = 4
print(mySol.solveNQueens(n))