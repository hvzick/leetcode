'''You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        n = len(s)
        for i in range(0, n-1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score

mySol = Solution()
s = "hello"
print(mySol.scoreOfString(s))
