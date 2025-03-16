'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.'''
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashMap = {}                           # Dictionary to store last seen index of each number
        for index, number in enumerate(nums):
            if number in hashMap and index - hashMap[number] <= k:
                return True                    # Found duplicate within range
            hashMap[number] = index            # Update index of current number
        return False                           # No such pair found
    
mySol = Solution()
nums = [1,2,3,1]
k = 3
print(mySol.containsNearbyDuplicate(nums, k))