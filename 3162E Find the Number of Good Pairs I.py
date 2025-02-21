'''You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.'''

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        ctr = 0                                 # initialise a counter
        for i in nums1:                         # loop over numbers in nums1 list 
                for j in nums2:                 # loop over numbers in nums2 list
                    if i % (j * k) == 0:        # check if current number of nums1 is perfectly divisible by current number of nums2 * k
                        ctr += 1                # increment the counter
        return ctr                              # return the counter

mySol = Solution()
nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
print(mySol.numberOfPairs(nums1, nums2, k))