'''Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.'''

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:  # check if numbers are equal
                    count += 1          # increment the counter
        return count

mySol = Solution()
nums = [1,2,3,1,1,3]
print(mySol.numIdenticalPairs(nums))