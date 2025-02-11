'''Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)                         # convert num1 to set
        s2 = set(nums2)                         # convert num2 to set
        l = s1 & s2 # s1.intersection(s2)       # use set intersection and store it in l
        x = list(l)                             # convert set l to list and store it in x
        return x                                # return the list

mySol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(mySol.intersection(nums1, nums2))