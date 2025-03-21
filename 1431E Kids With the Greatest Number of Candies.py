'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.'''

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        b = []
        m = max(candies)
        for i in candies:
            if i + extraCandies >= m:   # check if current candies + extra candies would be >= to the max candies in the list
                b.append(True)
            else:
                b.append(False)
        return b

mySol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(mySol.kidsWithCandies(candies, extraCandies))