class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, row, col):
            if col > 8:
                return backtrack(board, row + 1, 0)
            elif row > 8:
                return True
            if board[row][col] == '.':
                for number in range(1, 10):
                    if isSafe(board, row, col, str(number)):
                        board[row][col] = str(number)
                        if backtrack(board, row, col + 1):
                            return True
                        board[row][col] = '.'
                return False
            else:
                if backtrack(board, row, col + 1):
                    return True
            
        def isSafe(board, row, col, number):
            if (row + 3) // 3 == 1:
                r = 0
            elif (row + 3) // 3 == 2:
                r = 3
            else:
                r = 6
            if (col + 3) // 3 == 1:
                c = 0
            elif (col + 3) // 3 == 2:
                c = 3
            else:
                c = 6
            # check quadrant
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] == number:
                        return False
            for i in range(0, 9):
                if board[row][i] == number or board[i][col] == number:
                    return False
            return True
        backtrack(board, 0, 0)
        print(board)
mySol = Solution()
board = [
    [".",".",".",".","5",".",".","7","."],
    [".","9",".",".","4",".",".",".","."],
    [".",".","4",".",".",".",".",".","8"],
    [".","7","1",".",".","2",".",".","5"],
    [".","4",".",".",".",".","7",".","6"],
    ["2",".","6","4",".",".",".","9","."],
    [".",".",".",".","8","6",".",".","."],
    ["9",".","5",".",".",".",".",".","."],
    [".",".","3",".","7",".","2","5","."]
]
print(mySol.solveSudoku(board))
print(board)