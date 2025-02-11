'''In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.'''

class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        t = []
        r = []
        for i in range(0, n):
            if nums[i] not in t:
                t.append(nums[i])
            elif nums[i] in t:
                r.append(nums[i])
        return r

mySol = Solution()
nums = [0,1,1,0]
print(mySol.getSneakyNumbers(nums))