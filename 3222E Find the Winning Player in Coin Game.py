'''You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.

Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a total value 115. If the player is unable to do so, they lose the game.

Return the name of the player who wins the game if both players play optimally.'''

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        while True:                 
            if x < 1 or y < 4:      # check is 75 coins are not less than 1 and 10 coins are not less than 4
                return 'Bob'        # return bob because alice wasnt able to sum up tp 115
            x -= 1                  # decrement x by 1
            y -= 4                  # decrement y by 4
            if x < 1 or y < 4:      # check is 75 coins are not less than 1 and 10 coins are not less than 4
                return 'Alice'      # return alice because bob wasnt able to sum up tp 115
            x -= 1                  # decrement x by 1
            y -= 4                  # decrement y by 4

mySol = Solution()
x = 4
y = 11
print(mySol.winningPlayer(x, y))
