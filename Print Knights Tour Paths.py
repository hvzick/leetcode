class Solution:
    def checkValidGrid(self, board: list[list[int]]) -> bool:
        ans = []
        n = len(board)
        count = 0
        def nt(row, col, c):
            nonlocal count
            board[row][col] = c
            if c == n * n - 1:
                count += 1
                print(f"\nTour {count}:")
                ans.append([r[:] for r in board])
                for r in board:
                    print(r)
                board[row][col] = -1
                return
            if row + 2 < n and col + 1 < n:  # noqa: SIM102
                if board[row + 2][col + 1] == -1:
                    nt(row + 2, col + 1, c + 1)
                
            if row - 1 >= 0 and col - 2 >= 0:  # noqa: SIM102
                if board[row - 1][col - 2] == -1:
                    nt(row - 1, col - 2, c + 1)
            
            if row - 2 >= 0 and col + 1 < n:  # noqa: SIM102
                if board[row - 2][col + 1] == -1:
                    nt(row - 2, col + 1, c + 1)
                
            if row - 1 >= 0 and col + 2 < n:  # noqa: SIM102
                if board[row - 1][col + 2] == -1:
                    nt(row - 1, col + 2, c + 1)
                        
            if row - 2 >= 0 and col - 1 >= 0:  # noqa: SIM102
                if board[row - 2][col - 1] == -1:
                    nt(row - 2, col - 1, c + 1)
                
            if row + 2 < n and col - 1 >= 0:  # noqa: SIM102
                if board[row + 2][col - 1] == -1:
                    nt(row + 2, col - 1, c + 1)
                        
            if row + 1 < n and col + 2 < n:  # noqa: SIM102
                if board[row + 1][col + 2] == -1:
                    nt(row + 1, col + 2, c + 1)
                
            if row + 1 < n and col - 2 >= 0:  # noqa: SIM102
                if board[row + 1][col - 2] == -1:
                    nt(row + 1, col - 2, c + 1)
            board[row][col] = -1

        nt(0, 0, 0)
        print(f"\nTotal tours found: {count}")

mySol = Solution()
n = 5
board = [[-1] * n for _ in range(n)]
print(mySol.checkValidGrid(board))