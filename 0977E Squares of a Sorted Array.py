'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        L, R = 0, n-1
        result = [0] * n
        for i in range(n-1, -1, -1):            # loop in reverse
            if abs(nums[L]) > abs(nums[R]):     # check if number at left pointer is the greater than number at right pointer
                val = nums[L]                   # save number in val
                L += 1                          # increment left pointer
            else:
                val = nums[R]                   # save number in val
                R -= 1                          # decrement right pointer
            result[i] = val ** 2                # at the square to result list in reverse 
        return result

mySol = Solution()
nums = [-4,-1,0,3,10]
print(mySol.sortedSquares(nums))