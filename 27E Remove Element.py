class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        if len(nums) == 0:
            return 0 
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k        

mySol = Solution()
nums = [3,2,2,3]
val = 3
print(mySol.removeElement(nums, val))