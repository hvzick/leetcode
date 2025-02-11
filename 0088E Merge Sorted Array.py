'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 1 and nums1[0] == 0:   # check if there is space for only 1 element in nums1
            nums1[0] = nums2[0]                 # directly add the element from nums2 to nums1
        b = 0
        for i in range(m, len(nums1)):          # iterate from m to length of nums1
            nums1.insert(i, nums2[b])           # insert element from nums2 in nums1 in place of 0
            b += 1                              # increment pointer of nums2
            nums1.pop()                         # delete 0 from nums1 each time you add an element from nums1
        nums1.sort()                            # sort the list
        # print(nums1)

mySol = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
mySol.merge(nums1, m, nums2, n)