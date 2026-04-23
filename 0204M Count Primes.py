'''Given an integer n, return the number of prime numbers that are strictly less than n.'''

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n                  # Assume all numbers are prime initially.
        primes = 0                            # Counts primes found below n.
        for i in range(2, n):                 # Check each number from 2 to n-1.
            if isPrime[i]:                    # If still marked prime, count it.
                primes += 1                   # Increment prime counter.
                for j in range(i * 2, n, i):  # Mark all multiples of i as non-prime.
                    isPrime[j] = False        # Composite number detected.
        return primes                         # Return total number of primes.

mySol = Solution()                            # Create solution object.
n = 10                                        # Input limit (count primes less than 10).
print(mySol.countPrimes(n))                   # Expected output: 4 (2, 3, 5, 7).