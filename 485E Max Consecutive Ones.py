'''Given a binary array nums, return the maximum number of consecutive 1's in the array.'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        c = []
        for i in nums:
            if i == 1:          # if current number is 1
                count += 1      # increment the count
            c.append(count)     # append count to the list
            if i == 0:          # if current number is 0
                count = 0       # reset the count`
        return max(c)           # return maximum number in c list

mySol = Solution()
nums = [1,1,0,1,1,1]
print(mySol.findMaxConsecutiveOnes(nums))