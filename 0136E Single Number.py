class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0          # Initialize result to 0, which will hold the final single number
        for i in nums:      # Iterate through each number in the input list
            result ^= i     # Use the XOR operator to combine the numbers. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. This way, pairs of identical numbers will cancel each other out, leaving only the single number.
        return result       # Return the single number that appears only once in the array



mySol = Solution()
nums = [2,2,1]
print(mySol.singleNumber(nums))