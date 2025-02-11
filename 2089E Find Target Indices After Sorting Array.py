'''You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.'''

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
                index = []                      # initialise the index list
                nums.sort()                     # sort the nums list
                r = len(nums)-1                 # last index
                s = len(nums)//2                # divide lenth in half to iterate from front and back
                if len(nums) % 2 != 0:          # check if length of the list is odd
                    if nums[s] == target:       # check if the number at middle index is target
                        index.append(s)         # directly add that index to the index list
                for l in range(0, s):           # iterate over the left half of the list also the right pointer will iterate in negative direction
                    if nums[l] == target:       # check if number at current index is the target
                        index.append(l)         # add that undex to the list
                    if nums[r] == target:       # check if number at current index is the target
                        index.append(r)         # add that undex to the list
                    r -= 1                      # decrement right pointer
                index.sort()                    # sort the index list
                return index                    # return

mySol = Solution()
x = [1,2,2,3,5]
nums = [1,2,5,2,3]
nums = [65,93,31,62,84,16,44,71,100,13,
        61,75,54,42,50,74,11,73,79,75,
        6,92,26,65,88,56,34,85,91,16,
        24,80,93,51,55,73,87,64,63,91,
        92,97,89,53,38,93,73,50,54,98,
        18,5,7,65,35,97,81,37,81,12,
        23,17,83,83,74,46,94,97,8,14,
        93,59,12,87,93,63,91,28,29,64,
        84,66,11,39,9,18,10,33,77,62,
        88,91,89,91,7,77,85,61,49,8]
nums.sort()
print(nums)
target = 64
print(mySol.targetIndices(nums, target))