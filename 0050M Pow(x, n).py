'''#TODO Implement pow(x, n), which calculates x raised to the power n (i.e., xn).'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:                      # Any number raised to the power of 0 is 1
            return 1.0                  # Handle negative powers by taking the reciprocal of x and using the positive exponent
        binaryForm = n                  # Store the original value of n to handle negative powers
        if n < 0:                       # If n is negative, we take the reciprocal of x and convert n to positive
            x = 1 / x                   # Take the reciprocal of x for negative powers
            binaryForm = - binaryForm   # Convert n to positive for the loop to work correctly
        answer = 1                      # Initialize answer to 1, which will hold the final result                  
        while binaryForm > 0:           # Loop until all bits of the exponent have been processed
            if binaryForm % 2 == 1:     # If the least significant bit of binaryForm is 1, we multiply the current answer by x
                answer *= x             # Square x for the next bit of the exponent
            x *= x
            binaryForm //= 2            # Use integer division to avoid float result
        return answer                   # Return the final result after processing all bits of the exponent

mySol = Solution()
x = 2.00000
n = 10
print(mySol.myPow(x, n))