'''You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n^2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.'''

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        l = []
        result = list(range(1, n**2 + 1))    
        for i in range(0, n):
            for j in range(0, n):
                l.append(grid[i][j])
        for i in l:
            if l.count(i) > 1:
                a = i
        y = set(result) - set(l)
        b = list(y)
        x = b[0]
        nums = []
        nums.append(a)
        nums.append(x)
        return nums

mySol = Solution()
grid = [[9,1,7],
        [8,9,2],
        [3,4,6]]
print(mySol.findMissingAndRepeatedValues(grid))