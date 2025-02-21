'''You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.

The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.

Return the permutation difference between s and t.'''
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        permutationDifference = 0                                       # initialise a variable to count the difference
        hashMap1 = {}                                                   # initialise a dictionary to store index and values of s string
        hashMap2 = {}                                                   # initialise a dictionary to store index and values of t string
        for i in range(0, len(s)):                                      # loop over s string
            hashMap1[s[i]] = i                                          # add values to the dictionary with key as the value of s string and value its corresponding index in s string
            hashMap2[t[i]] = i                                          # add values to the dictionary with key as the value of t string and value its corresponding index in t string
        for key in hashMap1:                                            # loop over hash map
            permutationDifference += abs(hashMap1[key] - hashMap2[key]) # add the difference of two value of different dictionaries to the variable
        return permutationDifference                                    # return the permutation difference

mySol = Solution()
s = "abc"
t = "bac"
print(mySol.findPermutationDifference(s, t))