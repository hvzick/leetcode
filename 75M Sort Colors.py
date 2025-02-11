'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):         # use simple bubble sort to sort the list
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums




mySol = Solution()
nums = [2,0,2,1,1,0]
print(mySol.sortColors(nums))