'''You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.'''

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        i = 0
        count = 0
        for i in nums:
            if i % 3 == 0:
                pass
            else:
                count += 1
        return count

mySol = Solution()
nums = [1,2,3,4]
print(mySol.minimumOperations(nums))