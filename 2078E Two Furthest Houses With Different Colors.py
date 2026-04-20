'''There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.'''

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        m = 0
        for i in range(0, len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    m = max(abs(i - j), m)
        return m

        
mySol = Solution()
colors = [1,8,3,8,3]
print(mySol.maxDistance(colors))