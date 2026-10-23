'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        def dfs(res, idx, nums):
            if idx == n:
                return res.append(nums.copy())
            for i in range(idx, n):
                swap(idx, i, nums)
                dfs(res, idx + 1, nums)
                swap(idx, i, nums)
        def swap(a, b, nums):
            t = nums[a]
            nums[a] = nums[b]
            nums[b] = t
        dfs(res, 0, nums)
        return res
            
mySol = Solution()
nums = [1,2,3]
print(mySol.permute(nums))