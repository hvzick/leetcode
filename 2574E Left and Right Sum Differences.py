'''Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.'''

class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        ls = []
        rs = []
        ans = []
        n = len(nums)
        for i in range(0, n):
            ls.append(sum(nums[:i]))        # calculate sum of numbers of the left side of i
            rs.append(sum(nums[i+1:]))      # calculate sum of numbers of the lright side of i
            ans.append(abs(ls[i] - rs[i]))  # calculate |ls[i] - rs[i]|
        return ans                          # return answer list

mySol = Solution()
nums = [10,4,8,3]
print(mySol.leftRightDifference(nums))