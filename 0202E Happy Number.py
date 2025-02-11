'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''

class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        new = 0
        while True:
            for i in n:
                new += int(i) ** 2
            # print(new)
            if new == 1 or new == 7:
                return True
            if new == 4:
                return False
            n = str(new)
            if new == 1:
                return True
            new = 0

mySol = Solution()
n = 12
print(mySol.isHappy(n))
print(mySol.isHappy(19))
print(mySol.isHappy(100))