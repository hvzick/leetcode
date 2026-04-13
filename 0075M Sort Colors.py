'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)                       # get array size
        left = 0                            # boundary for next 0 placement
        mid = 0                             # current index being processed
        right = n - 1                       # boundary for next 2 placement
        while mid <= right:                 # process until unknown region is exhausted
            if nums[mid] == 0:              # move 0 to the left region
                temp = nums[mid]            # store current value
                nums[mid] = nums[left]      # bring left-region value to mid
                nums[left] = temp           # place 0 into left region
                left += 1                   # expand left (0s) region
                mid += 1                    # advance since swapped-in value is handled
            elif nums[mid] == 1:            # 1 is already in correct middle region
                mid += 1                    # just move forward
            elif nums[mid] == 2:            # move 2 to the right region
                temp = nums[mid]            # store current value
                nums[mid] = nums[right]     # bring right-region value to mid
                nums[right] = temp          # place 2 into right region
                right -= 1                  # shrink right (2s) region




mySol = Solution()                          # create solution object
nums = [2,0,2,1,1,0]                        # sample input
print(mySol.sortColors(nums))               # function returns None (array is modified in-place)