'''You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.

Example 1:

Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
Example 2:

Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.'''
import math

class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(x):                                      # Function to check if a number is prime
            if x <= 1:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True
        p = []
        n = len(nums)
        for i in range(n):                                      # Loop over the matrix to check both diagonals
            if is_prime(nums[i][i]):                            # Check the primary diagonal (nums[i][i])
                p.append(nums[i][i])
            if is_prime(nums[i][n - 1 - i]):                    # Check the secondary diagonal (nums[i][n - 1 - i])
                p.append(nums[i][n - 1 - i])
        if p:                                                   # If there are primes in the diagonals, return the maximum, otherwise return 0
            return max(p)
        return 0 

mySol = Solution()
nums = [[1,2,3],
        [5,17,7],
        [9,11,10]]
nums = [[1,2,3],[5,6,7],[9,10,11]]
print(mySol.diagonalPrime(nums))