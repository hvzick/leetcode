'''You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.

Return the total number of beautiful pairs in nums.

Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.
'''

from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        n = len(nums)
        counter = 0
        for i in range(0, n-1):                 
            for j in range(i+1, n):
                l = str(nums[i])[0]                 # convert int to string to check the left number 
                r = str(nums[j])[-1]                # convert int to string to check the right number
                if gcd(int(l), int(r)) == 1:        # convert l and r to int, then check if they are co-primes or not
                    counter += 1                    # increment counter each time we get a co-prime
        return counter

mySol = Solution()
nums = [2,5,1,4]
print(mySol.countBeautifulPairs(nums))