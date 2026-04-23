'''You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n^2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.'''

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)                                                       # Grid size is n x n.
        limit = n * n                                                       # Values should be in range 1..n^2.
        actualSum = 0                                                       # Sum of values present in grid.
        actualSquareSum = 0                                                 # Sum of squares of values in grid.
        for i in range(0, n):                                               # Traverse each row.
            for j in range(0, n):                                           # Traverse each column.
                value = grid[i][j]                                          # Current cell value.
                actualSum += value                                          # Accumulate normal sum.
                actualSquareSum += value * value                            # Accumulate square sum.
        expectedSum = (limit * (limit + 1)) // 2                            # Sum of numbers from 1 to n^2.
        expectedSquareSum = (limit * (limit + 1) * ((2 * limit) + 1)) // 6  # Square sum of 1..n^2.
        diff = actualSum - expectedSum                                      # repeated - missing.
        squareDiff = actualSquareSum - expectedSquareSum                    # repeated^2 - missing^2.
        sumRM = squareDiff // diff                                          # repeated + missing.
        repeated = (diff + sumRM) // 2                                      # Solve for repeated number.
        missing = repeated - diff                                           # Solve for missing number.
        return [repeated, missing]                                          # Return [repeated, missing].


mySol = Solution()                                                          # Create solution object.
grid = [[9, 1, 7],                                                          # Sample grid with duplicate and missing values.
    [8, 9, 2],
    [3, 4, 6]]
print(mySol.findMissingAndRepeatedValues(grid))