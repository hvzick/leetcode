'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums_set = set(nums)            # convert the list to set to remove duplicates
        missing = []                    # initialise the missing list
        for i in range(1, n+1):         # loop from 1 to n
            if i not in nums_set:       # check if current index number is not in the nums list
                missing.append(i)       # append the index to the missing list
        return missing                  # return the list

mySol = Solution()
nums = [1,1]
print(mySol.findDisappearedNumbers(nums))
