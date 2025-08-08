'''#TODO You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.  
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)                          # number of houses
        if n == 0: return 0                    # no houses -> 0
        if n == 1: return nums[0]              # single house -> rob it
        dp = [0] * n                           # dp[i] = max money up to i
        dp[0] = nums[0]                        # first house only
        dp[1] = max(nums[0], nums[1])          # choose better of first two
        for i in range(2, n):                  # fill dp from house 2 onward
            dp[i] = max(dp[i-1],               # skip current house
                        dp[i-2] + nums[i])     # rob current + dp[i-2]
        print(dp)                              # debug: full dp array
        return dp[-1]                          # answer: last entry
    
mySol = Solution()
nums = [2,7,9,3,1]
print(mySol.rob(nums))