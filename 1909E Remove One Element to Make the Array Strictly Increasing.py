'''Given a 0-indexed integer array nums, return true if it can be made strictly increasing
after removing exactly one element, or false otherwise. If the array is already strictly 
increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each 
index (1 <= i < nums.length).'''

class Solution:
    def canBeIncreasing(self, n: list[int]) -> bool:
        ctr = 0
        nums = n.copy()
        if len(nums) == 2:
            return True
        if len(set(nums)) == 1:
            return False
        if nums == sorted(nums):
            return True
        for i in range(1, len(n)):
            # print(nums[i-1], nums[i]) 
            # print(f"i-1 = {i-1}\ni   = {i}")
            if nums[i-1] > nums[i]:
                ctr += 1
                if ctr > 1:
                    return False
                nums.pop(i)
                #print(f'i-1 = {i-1} and i = {i}')
                if nums == sorted(nums):
                        if nums.count(nums[i-1]) > 1 and len(nums) > 2:
                            return False
                        else:
                            return True
                nums = n.copy()
                nums.pop(i-1)
                if nums == sorted(nums):
                        if nums.count(nums[i-1]) > 1 and len(nums) > 2:
                            return False
                        else:
                            return True
                else:
                    return False
            nums = n.copy()
            if len(nums) > 2 and nums[i-1] == nums[i]:
                return False

mySol = Solution()
nums1 = [105,924,32,968]
nums2 = [100,21,3]
nums3 = [1,2,1,3]
print(mySol.canBeIncreasing(nums1))
print(mySol.canBeIncreasing(nums2))
print(mySol.canBeIncreasing(nums3))