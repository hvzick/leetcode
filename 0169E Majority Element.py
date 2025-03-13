'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()             # sort the list
        mid = len(nums) // 2    # check the middle index because the list contains atleast one number whose frequency is greater then n/2
        return nums[mid]        # return middle element

mySol = Solution()
nums = [2,2,1,1,1,2,2]
print(mySol.majorityElement(nums))