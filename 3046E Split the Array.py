'''You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:

nums1.length == nums2.length == nums.length / 2.
nums1 should contain distinct elements.
nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise.'''
class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        hashMap = {}
        for i in range(0, len(nums)):       # loop over the nums
            if nums[i] not in hashMap:      # check if current number is not in the hash map
                hashMap[nums[i]] = 1        # add it to the hash map as key and its frequency as value
            else:                           # if the  number is already is the hash map
                hashMap[nums[i]] += 1       # increment the value by 1
            if hashMap[nums[i]] > 2:        # if the frequency of any number is greater than two
                return False                # return false because the array cant be split without having duplicates
        return True                         # return true

mySol = Solution()
nums = [1,1,2,2,3,4]
print(mySol.isPossibleToSplit(nums))