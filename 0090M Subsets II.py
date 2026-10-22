'''Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order. '''

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        ans = []
        def dfs(i):
            if len(nums) == i:
                return res.append(ans.copy())
            ans.append(nums[i])                 # Include
            dfs(i + 1)
            ans.pop()                           # Exclude
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: # skip same digits
                i += 1
            dfs(i + 1)
        dfs(0)
        return res
    
mySol = Solution()
nums = [4,4,4,1,4]
print(mySol.subsetsWithDup(nums))