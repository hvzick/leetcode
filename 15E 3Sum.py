'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        c = []
        nums.sort()                                                 # sort the list
        n = len(nums)
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:                      # Skip duplicate elements
                continue
            k = n-1
            j = i + 1
            while j < k:
                r = []
                if j < k: 
                    if nums[i] + nums[j] + nums[k] == 0:            # if sum == 0 
                        r.append(nums[i])                           # append elements to the list
                        r.append(nums[j]) 
                        r.append(nums[k])   
                        c.append(r)                                 # append list to triplets to another list
                        while j < k and nums[j] == nums[j + 1]:     # Skip duplicate elements
                            j += 1                                  # increment left pointer
                        while j < k and nums[k] == nums[k - 1]:     # Skip duplicate elements
                            k -= 1                                  # decrement right pointer
                        j += 1                                      # increment left pointer
                        k -= 1                                      # decrement right pointer
                    elif nums[i] + nums[j] + nums[k] < 0:           # if sum > 0 
                        j += 1                                      # increment left pointer
                    elif nums[i] + nums[j] + nums[k] > 0:           # if sum is > 0
                        k -= 1                                      # decrement right pointer
        return c

mySol = Solution()
nums = [-1,0,1,2,-1,-4]
print(mySol.threeSum(nums))