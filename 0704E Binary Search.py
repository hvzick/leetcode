class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1



mySol = Solution()
nums1 = [1,0]
target1 = 0
nums2 = [-1,0,3,5,9,12]
target2 = 2
print(mySol.search(nums1, target1))
# print(mySol.search(nums2, target2))