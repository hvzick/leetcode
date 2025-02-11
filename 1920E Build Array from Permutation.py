'''Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).'''

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []                                # initialise new list
        for i in range(0, len(nums)):           # loop over the nums list
            ans.append(nums[nums[i]])           # append number at nums[i] index to the new list
        return ans                              # return the new list

mySol = Solution()
nums = [0,2,1,5,3,4]
print(mySol.buildArray(nums))