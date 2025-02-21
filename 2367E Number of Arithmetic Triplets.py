'''You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.'''
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        ctr = 0                                         # initialise a counter 
        for i in range(0, len(nums)):                   # start loop from 0
            for j in range(i+1, len(nums)):             # start loop from i + 1
                if nums[j] - nums[i] == diff:           # if condition is true then only we need to proceed further
                    for k in range(j+1, len(nums)):     # start loop from j + 1
                        if nums[k] - nums[j] == diff:   # if condition is true then enter the if block
                            ctr += 1                    # increment the counter
        return ctr                                      # return the counter

mySol = Solution()
nums = [0,1,4,6,7,10]
diff = 3
print(mySol.arithmeticTriplets(nums, diff))