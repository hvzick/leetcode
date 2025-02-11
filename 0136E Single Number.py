class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i 
        return result



mySol = Solution()
nums = [2,2,1]
print(mySol.singleNumber(nums))