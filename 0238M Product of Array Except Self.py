''' #TODO Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.'''



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = len(nums) * [1]                        # prefix products initialized to 1
        suffix = len(nums) * [1]                        # suffix products initialized to 1
        product = []                                    # result array
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]     # build prefix product for each index
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]     # build suffix product for each index
        for i in range(0, len(nums)):
            product.append(prefix[i] * suffix[i])        # multiply prefix and suffix for result
        return product                                   # return the result array

mySol = Solution()
nums = [1,2,3,4]
print(mySol.productExceptSelf(nums))