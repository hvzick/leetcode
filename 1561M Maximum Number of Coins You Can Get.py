'''There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.'''

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)            # sort the piles in descending order
        me = 0                              # initialise counter from 0
        y = 1                               # initialise index which will keep track of the index of my numbers
        for a in range(0, n//3):            # we will get the piles always in multiple of 3 so we have to iterate till n//3 because each person will take 1 number n//3 times
            me += piles[y]                  # add the number which i will take
            y += 2                          # increment by 2 because the next is gonna be taken by Alice
        return me                           # return the max numbers that i can take

mySol = Solution()
piles = [9,8,7,6,5,1,2,3,4]
print(mySol.maxCoins(piles)) 