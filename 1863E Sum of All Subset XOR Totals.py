'''The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.'''
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(i, total):
            print(f'I = {i}, total = {total}')
            if i == len(nums):                      # base case for returning back when we are at last element
                print('return back', total)
                return total                        # return back
            include = dfs(i + 1, total ^ nums[i])   # when we include all numbers
            notInclude = dfs(i + 1, total)          # when we dont include current number
            return include + notInclude             # sum both
        return dfs(0, 0)                            # return the sum

mySol = Solution()
nums = [5,1,6]
print(mySol.subsetXORSum(nums))