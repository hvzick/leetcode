'''You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.'''

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        n = len(nums)
        counter = 0
        new = nums.copy()                   # crete copy of the original list
        new.sort(reverse=True)              # sort the copy in rverse order
        for i in range(1, n):               # loop from index 1 to n-1
            if new[0] >= 2 * new[i]:        # check if largest element at index 0 is twice the other numbers
                counter += 1                # increment the counter
        if counter == n - 1:                # if the counter is equal to n-1 which means the largest number is twice the other numbers
            return nums.index(new[0])       # return the index of that number from original list
        else:
            return -1                       # else return -1

mySol = Solution()
nums = [3,6,1,0]
print(mySol.dominantIndex(nums))