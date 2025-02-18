'''ou're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in jewels:            # loop over jewels
            for j in stones:        # loop over stones
                if i == j:          # compare each jewel with each stone
                    counter += 1    # of there's a match increment the counter
        return counter              # return the counter

mySol = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(mySol.numJewelsInStones(jewels, stones))