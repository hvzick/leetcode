'''
#TODO A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array. You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low = 0                                                  # left boundary
        high = len(arr) - 1                                      # right boundary
        while low < high:                                        # keep narrowing to one index
            mid = low + (high - low) // 2                       # midpoint
            if arr[mid] < arr[mid + 1]:                         # still on rising slope
                low = mid + 1                                    # peak is to the right
            else:
                high = mid                                       # peak is at mid or to the left
        return low                                               # low == high is the peak index



mySol = Solution()
arr = [18,29,38,59,98,100,99,98,90]
print(mySol.peakIndexInMountainArray(arr))