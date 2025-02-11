'''Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.'''

class Solution:
    def getConcatenation(self, nums:list[int]) -> list[int]:
        i = 0
        l = len(nums)
        for i in range(1, l, 2):                                  # loop over the nums list increment by 2
            nums.append(nums[i-1])                                # append element at i-1 index 
            nums.append(nums[i])                                  # append element at ith index
        if l % 2 != 0:                                            # if the length of list is odd 
            nums.append(nums[l-1])                                # appends the l-1 elemnt to the list
        return nums                                             # return nums list

mySol = Solution()
nums = [1,2,3]
print(mySol.getConcatenation(nums))