'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(0, len(nums)+1):     # loop over all n numbers
            if i not in nums:               # if any number is missing 
                return i                    # return that number

mySol = Solution()
nums = [3,0,1]
print(mySol.missingNumber(nums))