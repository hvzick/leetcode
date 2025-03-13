'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        for i in nums1:
            if i in nums2:              # check if current number of nums2 is in nums1
                nums2.remove(i)         # remove the number from nums2
                intersection.append(i)  # append it to the intersection list
        return intersection

mySol = Solution()
nums1 = [1,2,2,1] 
nums2 = [2,2]
print(mySol.intersect(nums1, nums2))