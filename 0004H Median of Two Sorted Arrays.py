'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).'''
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2                   # merge the two lists                   
        nums3.sort()                            # sort the merged list
        if len(nums3) % 2 != 0:                 # when length of the merged list is odd
            return nums3[len(nums3)//2]         # return middle element
        else:                                   # when length of the merged list is even
            n2 = len(nums3) // 2                # find the second middle index 
            n1 = (len(nums3) // 2) - 1            # find the first middle index
            return (nums3[n1] + nums3[n2]) / 2  # return mean of two middle numbers

mySol = Solution()
nums1 = [2,2,4,4]
nums2 = [2,2,2,4,4]
print(mySol.findMedianSortedArrays(nums1, nums2))
