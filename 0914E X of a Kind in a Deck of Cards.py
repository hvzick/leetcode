'''You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.'''
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        hashMap = {}
        for i in range(0, len(deck)):   # create hashmap with key as the number and value as its frequency
            if deck[i] not in hashMap:
                hashMap[deck[i]] = 1
            else:
                hashMap[deck[i]] += 1
        temp = list(hashMap.values())   # store frequencies in a list
        for i in temp:                  
            for j in temp:
                if gcd(i, j) < 2:       # a valid partition requires that we can divide all counts into equal-sized groups of at least x ≥ 2
                    return False
        return True

mySol = Solution()
deck = [1,2,3,4,4,3,2,1]
# deck = [1,1,1,2,2,2,3,3]
print(mySol.hasGroupsSizeX(deck))