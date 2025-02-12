'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        root = 0
        while l <= x:           # iterate over numbers till x
            if l*l <= x:        # check if product of currrent number is less or equal to x
                root = l        # store the number in root
                l += 1          # increment l
            else:               # if product of currrent number is not less or equal to x
                return root     # return root
        return root             # return root incase the loop ends without entering the else statement

mySol = Solution()
x = 1
print(mySol.mySqrt(x))
