class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)
        r = n-1
        c1, c2 = 0, 0
        for l in range(0, n):
            if nums[l] < 0:     # for -ve integers
                c1 += 1
            if nums[r] > 0:     # for +ve integers
                c2 += 1
                r -= 1
        if c1 > c2: return c1 
        else: return c2

mySol = Solution()
nums = [-2,-1,-1,1,2,3]
print(mySol.maximumCount(nums))