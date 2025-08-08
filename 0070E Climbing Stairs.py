'''#TODO 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n                     # base cases: f(1)=1, f(2)=2, f(3)=3
        current = 0                             # placeholder for f(i)
        previous1 = 3                           # f(3)
        previous2 = 2                           # f(2)
        for i in range(3, n):                   # iterate from 3 up to n-1
            current = previous1 + previous2     # f(i+1) = f(i) + f(i-1)
            previous2 = previous1               # shift previous2 to previous f(i)
            previous1 = current                 # update previous1 to new f(i+1)
        return current                          # total ways for n steps

mySol = Solution()
n = 45
print(mySol.climbStairs(n))