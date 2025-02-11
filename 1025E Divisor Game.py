'''Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.'''

class Solution:
    def divisorGame(self, n: int) -> bool:
        c = 0
        x = 1
        while True:
            if 0 < x < n and n % x == 0:    # check if n lies between 0 and n and n is perfectly divisible by x
                n = n - x                   # update n to n - x
                c += 1                      # increment c
            else:                      
                if c % 2 == 0:              # check if c is even
                    return False
                else:                                   
                    return True
        # odd tries = alice even tries = bob
        """or 
        if n % 2 == :
            return True
        else:
            return False
        """

mySol = Solution()
n = 2
print(mySol.divisorGame(n))