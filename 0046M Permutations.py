'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        def backtrack(idx):
            if idx == n:
                return res.append(nums.copy())
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(0)
        return res
            
mySol = Solution()
nums = [1,2,3]
print(mySol.permute(nums))