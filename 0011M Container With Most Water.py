'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)                              # get the number of lines
        l = 0                                        # initialize left pointer
        r = n - 1                                    # initialize right pointer
        area = 0                                     # variable to store max area
        while l < r:                                 # loop runs while left pointer is less than the right pointer
            if height[l] < height[r]:                # check if height of left is less than height of right
                area = max(area, (r-l) * height[l])  # calculate area using left height
                l += 1                               # increment left pointer
            elif height[l] == height[r]:             # check if height is equal
                area = max(area, (r-l) * height[l])  # calculate area using either height
                r -= 1                               # decrement right pointer
                l += 1                               # increment left pointer
            else:                                    # height of left is greater than height of right
                area = max(area, (r-l) * height[r])  # calculate area using right height
                r -= 1                               # decrement right pointer
        return area                                  # return the maximum area found

mySol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(mySol.maxArea(height))