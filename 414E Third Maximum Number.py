class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        nums = list(s)
        nums.sort(reverse=True)
        if len(nums) <= 2:
            return nums[0]
        else:
            return nums[2]
        
mySol = Solution()
nums = [5,2,2]
print(mySol.thirdMax(nums))