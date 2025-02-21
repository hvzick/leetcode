'''Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.'''

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        ctr = 0                                 # initialise a counter 
        for i in range(0, len(nums)):           # start loop from 0
            for j in range(i+1, len(nums)):     # start loop from i + 1
                if abs(nums[i] - nums[j]) == k: # check the condition
                    ctr += 1                    # increment the counter
        return ctr                              # return the counter
    
mySol = Solution()
nums = [1,2,2,1]
k = 1
print(mySol.countKDifference(nums, k))