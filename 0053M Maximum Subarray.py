'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -999999999                     # Initialize maxSum to a very small number to handle cases where all numbers are negative
        currentSum = 0                          # Keep track of the running sum for the current subarray
        for i in range(0, len(nums)):           # Loop through each number in the array
            currentSum += nums[i]               # Add the current number to the running sum
            maxSum = max(currentSum, maxSum)    # Update maxSum if currentSum is larger
            if currentSum < 0:                  # Reset if running sum becomes negative
                currentSum = 0                  # Start a new subarray from next index
        return maxSum                           # Return the maximum subarray sum found

mySol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(mySol.maxSubArray(nums))                  # Example with mixed positive and negative values
print(mySol.maxSubArray(nums=[-1]))             # Example where array has a single negative value