'''Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        r = []
        for i in range(0, n):
            c = 0
            for j in range(0, n):
                if nums[i] > nums[j]:
                    c += 1
            r.append(c)
        return r

mySol = Solution()
nums = [8,1,2,2,3]
print(mySol.smallerNumbersThanCurrent(nums))