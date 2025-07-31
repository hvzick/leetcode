'''
# TODO
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      l = 1                       # left ptr
      r = num                     # right ptr
      while l <= r:               # binary search loop
        mid = (l + r) // 2        # middle point
        num_squared = mid * mid
        if num_squared == num:    # perfect square found
           return True
        elif num_squared < num:   # mid too small
            l = mid + 1           # search left half
        else:                     # mid too large
            r = mid - 1           # search right half
      return False                # no perfect square
    

mySol = Solution()
num = 3086358025
print(mySol.isPerfectSquare(num))

