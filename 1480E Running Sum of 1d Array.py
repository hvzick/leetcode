'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        c = []
        summ = 0
        for i in range(0, n):
            summ += nums[i]
            c.append(summ)
        return c

mySol = Solution()
nums = [1,2,3,4]
print(mySol.runningSum(nums))