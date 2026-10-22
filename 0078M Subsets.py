'''Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.'''


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        i = 0
        ans = []
        def dfs(i):
            if len(nums) == i:
                return res.append(ans.copy())
            ans.append(nums[i])                 # Include
            dfs(i + 1)
            ans.pop()                           # Exclude
            dfs(i + 1)
        dfs(i)
        return res
    
mySol = Solution()
nums = [1,2,3]
print(mySol.subsets(nums))