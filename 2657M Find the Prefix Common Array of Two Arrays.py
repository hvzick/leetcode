'''You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
'''

class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        seenA = []                                          # keep track of elements seen at A
        seenB = []                                          # keep track of elements seen at B
        c = []                                              # used to store results and return it
        count = 0                                           # used to keep track of numbers
        for i in range(0, len(A)):                          # loop over any one of the list because they are of equal length
            if A[i] == B[i]:                                # when both elements are same
                count += 1                                  # increment by 1
                seenA.append(A[i])                          # append it to seen A
                seenB.append(A[i])                          # append it to seen B
                c.append(count)                             # append the count to the final list
                continue                                    # skip all lines
            if A[i] not in seenB:                           # when element of A is not seen in B
                seenB.append(A[i])                          # append to to seen at B
            if B[i] not in seenA:                           # when element of  is not seen in A
                seenA.append(B[i])                          # append to to seen at B
            count = len(set(seenA).intersection(set(seenB)))# check number of elements in both lists
            c.append(int(count))                            # append it to final listt
        return c                                            # return the final list

mySol = Solution()
A = [7, 1, 5, 3, 6, 2, 4]
B = [4, 2, 6, 3, 5, 1, 7]
print(mySol.findThePrefixCommonArray(A, B))

