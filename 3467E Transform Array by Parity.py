'''You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.'''
class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:    # check if number is odd
                nums[i] = 1         # replace with 1
            else:                   # when number is even
                nums[i] = 0         # replace with 0
        return sorted(nums)         # return sorted list

mySol = Solution()
nums = [4,3,2,1]
print(mySol.transformArray(nums))