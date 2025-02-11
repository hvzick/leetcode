'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:                   # loop until l <= r
            mid = (l + r) // 2
            if nums[mid] == target:     # if we find the number 
                return mid              # return its index
            elif nums[mid] > target:    # if current number is greater than the target
                r = mid - 1             
            else:                       # if current number is less than the target
                l = mid + 1
        return l                        # return the search index

mySol = Solution()
nums = [1,3,5,6]
target = 4
print(mySol.searchInsert(nums, target))