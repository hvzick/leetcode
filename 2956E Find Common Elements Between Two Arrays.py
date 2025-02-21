'''You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].'''

class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ctr = []                        # initialise a counter list
        temp = 0                        # initialise a temp variable
        for i in range(0, len(nums1)):  # loop over nums1 list
            if nums1[i] in nums2:       # check if nums1[i] is in nums2
                temp += 1               # increment the temp variable
        ctr.append(temp)                # append counter to the list
        temp = 0                        # reset temp variable to start counting again from 0
        for i in range(0, len(nums2)):  # loop over nums2 list
            if nums2[i] in nums1:       # check if nums2[i] is in nums1
                temp += 1               # increment the temp variable
        ctr.append(temp)                # append counter to the list
        return ctr                      # return the counter

mySol = Solution()
nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(mySol.findIntersectionValues(nums1, nums2))