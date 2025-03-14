'''You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
Return nums after the rearrangement.'''

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []                       # initialise list to store numbers less than pivot number
        piv = []                        # initialise list to store numbers equal to the pivot number
        greater = []                    # initialise list to store numbers greater than pivot number
        for i in nums:                  # loop over the given list
            if i < pivot:               # check if current number is less than the pivot number
                less.append(i)
            elif i == pivot:            # check if current number is equal to the pivot number
                piv.append(i)
            else:                       # check if current number is greater than the pivot number
                greater.append(i)
        final = less + piv + greater    # concatenate the lists in the same order 
        return final                    # return the final list
        

mySol = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
print(mySol.pivotArray(nums, pivot))

#  TOOK ME LESS THAN 5 MINUTES TO SOLVE