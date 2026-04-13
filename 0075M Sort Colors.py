'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        mid = 0
        right = n - 1
        while mid <= right:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[left]
                nums[left] = temp
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[right]
                nums[right] = temp
                right -= 1




mySol = Solution()
nums = [2,0,2,1,1,0]
print(mySol.sortColors(nums))