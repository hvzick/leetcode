'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n                             # initialize result array with 1s
        for i in range(1, n):                        # compute left product and store it in result
            result[i] = nums[i - 1] * result[i - 1]  # multiply previous left product
        rProduct = 1                                 # initialize right product
        for i in range(n-1, -1, -1):                 # traverse from right to left, multiplying with right product
            result[i] = result[i] * rProduct         # multiply current value with right product
            rProduct *= nums[i]                      # update right product for next iteration
        return result                                # Return final result array

mySol = Solution()
nums = [1,2,3,4]
print(mySol.productExceptSelf(nums))