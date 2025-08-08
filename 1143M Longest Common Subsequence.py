'''
#TODO Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde". A common subsequence of two strings is a subsequence that is common to both strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1                     # rows = |text1| + 1 (include empty prefix)
        cols = len(text2) + 1                     # cols = |text2| + 1 (include empty prefix)
        mat = [[0] * rows for _ in range(cols)]   # mat[i][j] = LCS len of text2[:i], text1[:j]
        for i in range(1, cols):                  # iterate text2 prefixes
            for j in range(1, rows):              # iterate text1 prefixes
                if text2[i - 1] != text1[j - 1]:  # chars differ
                    mat[i][j] = max(mat[i-1][j],  # skip current char of text2
                                     mat[i][j-1]) # or skip current char of text1
                else:                             # chars match
                    mat[i][j] = mat[i-1][j-1] + 1 # extend LCS by 1
        print(mat)
        return mat[-1][-1]                        # answer in bottom-right

mySol = Solution()
text1 = "abcde"
text2 = "ace"
print(mySol.longestCommonSubsequence(text1, text2))