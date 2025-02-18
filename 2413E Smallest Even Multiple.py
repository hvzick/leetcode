'''Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.'''

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else 2 * n   # If n is even → answer = n, If n is odd → answer = 2 * n

mySol = Solution()
print(mySol.smallestEvenMultiple(n=5))
print(mySol.smallestEvenMultiple(n=6))

