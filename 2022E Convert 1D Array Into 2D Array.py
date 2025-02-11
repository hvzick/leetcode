'''You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.'''

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):              # check if its possible to create a 2-D array
            return []                           # return empty list
        else:
            new = []
            k = 0                               # initialise starting index
            for i in range(0, m):
                temp = []
                for j in range(0, n):
                    temp.append(original[k])    # append n elements to each row
                    k += 1                      # keep track of indicies
                new.append(temp)                # append columns to the row
        return new



mySol = Solution()
original = [1,2,3,4]
m = 2
n = 2
print(mySol.construct2DArray(original, m, n))