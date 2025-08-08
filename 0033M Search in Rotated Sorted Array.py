''' #TODO
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0                                      # initialise left pointer
        r = len(nums) - 1                          # initialise right pointer
        while l <= r:                              # binary search loop
            mid = (l + r) // 2                     # mid index
            if nums[mid] == target:                # target found
                return mid
            elif nums[l] <= nums[mid]:             # left half is sorted
                if nums[l] <= target <= nums[mid]: # target lies in left half
                    r = mid - 1                    # move right pointer left
                else:                              # target not in left half
                    l = mid + 1                    # move left pointer right
            else:                                  # right half is sorted
                if nums[mid] <= target <= nums[r]: # target lies in right half
                    l = mid + 1                    # move left pointer right
                else:                              # target not in right half
                    r = mid - 1                    # move right pointer left
        return -1                                  # target not found

mySol = Solution()                                 # instance
nums = [4,5,6,7,0,1,2]                             # rotated sorted array
target = 0                                         # target value
print(mySol.search(nums, target))                  # output result