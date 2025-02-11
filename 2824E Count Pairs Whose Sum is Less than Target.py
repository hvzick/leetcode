'''Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.'''

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        counter = 0
        '''  O(n^2) time complexity
        for i in range(0, len(nums)-1):                   # loop from 0 to n-2
            for j in range(1, len(nums)):                 # loop from 1 to n-1
                if i < j and nums[i] + nums[j] < target:  # check if i < j and current numbers at those positions are less than target
                    counter += 1                          # increment by 1 whenever the condition is satisfied'''
        # O(nlogn)
        l = 0                                             # set l to the first index       
        r = len(nums)-1                                   # set r to the last index 
        nums.sort()                                       # sort the list
        while l <= r:                                     # loop till l <= r
            if nums[l] + nums[r] < target:                # if numbers at l and r are less than target
                counter += r - l                          # increment counter by l - r because all the elements in that range would be also less than target
                l += 1                                    # increment l by 1
            else:                                         # if numbers at l and r are not less than the target
                r -= 1                                    # decrement r by -1
        return counter                                    # return counter

mySol = Solution()
nums = [-1,1,2,3,1]
target = 2
nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(mySol.countPairs(nums, target))