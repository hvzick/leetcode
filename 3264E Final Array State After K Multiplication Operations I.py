'''You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	            Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
'''

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for j in range(0, k):
            x = min(nums)               # find the minimum number
            i = nums.index(x)           # get its index
            nums[i] = x * multiplier    # replace the number with  x * multiplier
        return nums

mySol = Solution()
nums = [2,1,3,5,6]
k = 5
multiplier = 2
print(mySol.getFinalState(nums, k, multiplier))