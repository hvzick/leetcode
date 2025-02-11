'''You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.'''

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = len(mat)
        d = {}
        x = []
        for i in range(0, m):                       # loop over the rows in matrix
            z = mat[i].count(1)                     # count the number of ones in each row
            d[i] = z                                # create a dictionary with row number as its key and count of ones as it value
        d = sorted(d.items(), key=lambda x: x[1])   # sort the dictionary based on the values of keys, it returns tuples within a list
        for i in range(0, k):                       # loop over the tuples upto k number
            x.append(d[i][0])                       # append first element of each tuple because thats they row value of the sorted values in the dictionary
        return x                                    # return the list with weakest rows

mySol = Solution()
matrix = [ [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k = 3
print(mySol.kWeakestRows(matrix, k))