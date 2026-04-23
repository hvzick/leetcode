'''
#TODO You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
'''

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)                                                         # total number of elements
        low = 0                                                               # left boundary of search
        high = n - 1                                                          # right boundary of search
        if n == 1: return nums[0]                                             # only one element means it is the answer
        while low <= high:                                                    # binary search loop
            mid = high + (low - high) // 2                                    # middle index (overflow-safe form)
            if mid == 0 and nums[0] != nums[1]:                               # unique element at the beginning
                return nums[mid]
            if mid == n - 1 and nums[n - 1] != nums[n - 2]:                   # unique element at the end
                return nums[mid]
            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:     # mid differs from both neighbors
                return nums[mid]
            if mid % 2 == 0:                                                  # even index case
                if nums[mid - 1] == nums[mid]:                                # pair alignment is broken on left side
                    high = mid - 1                                            # search left half
                else:
                    low = mid + 1                                             # search right half
            else:                                                             # odd index case
                if nums[mid - 1] == nums[mid]:                                # pair is valid through mid
                    low = mid + 1                                             # unique element is to the right
                else:
                    high = mid - 1                                            # unique element is to the left
        return - 1                                                            # fallback (should not happen for valid input)


mySol = Solution()                                                            # create solution instance
nums = [1,1,2,3,3,4,4,8,8]                                                    # sample input with single element 2
print(mySol.singleNonDuplicate(nums))                                         # expected: 2
print(mySol.singleNonDuplicate(nums=[1]))                                     # expected: 1
print(mySol.singleNonDuplicate(nums=[1,1,2]))                                 # expected: 2