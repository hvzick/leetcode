'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        c = []
        while l < r:                            # loop runs while left pointer is less than the right pointer
            if height[l] < height[r]:           # check if height of left is less than height of right
                area = (r-l) * height[l]        # calculate area
                l += 1                          # increment left
            elif height[l] == height[r]:        # check if height is equal
                area = (r-l) * height[l]        # calculate area
                l += 1                          # increment left
                r -= 1                          # decrement right
            else:                               # check if height of left is greater than height of right
                area = (r-l) * height[r]        # calculate area
                r -= 1                          # decrement right
            c.append(area)                      # append heights to the list in every iteration
        return max(c)

mySol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(mySol.maxArea(height))