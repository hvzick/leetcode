'''
#TODO Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''

class Solution:
    def largestPerimeter(self, nums: list[int])-> int:
        nums.sort(reverse=True)
        print(nums)
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2] and nums[i] + nums[i + 2] > nums[i + 1] and nums[i + 2] + nums[i + 1] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


mySol = Solution()
nums = [1,2,1,10]
print(mySol.largestPerimeter(nums))