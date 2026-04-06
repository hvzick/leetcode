'''You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.'''

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        answer = [0] * len(nums)
        evenIndex = 0
        oddIndex = 1
        for i in range(0, len(nums)):
            if nums[i] >= 0:
                answer[evenIndex] = nums[i]
                evenIndex += 2
            else:
                answer[oddIndex] = nums[i]
                oddIndex += 2
        return answer

mySol = Solution()
nums = [3,1,-2,-5,2,-4]
print(mySol.rearrangeArray(nums))
print(mySol.rearrangeArray(nums=[-1,1]))
print(mySol.rearrangeArray(nums=[-2,-5,-4,1,2,3]))