'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hs = {}
        for i in range(len(nums)):
            first = nums[i]
            second  = target - first
            if second in hs:
                return [i, hs[second]]
            else:
                hs[first] = i

mySol = Solution()
nums = [2,7,11,15]
target = 9
print(mySol.twoSum(nums, target))