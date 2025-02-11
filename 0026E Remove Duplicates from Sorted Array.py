class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        if len(nums) == 0:
            return 0 
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1

mySol = Solution()
nums = [1,1]
print(mySol.removeDuplicates(nums))