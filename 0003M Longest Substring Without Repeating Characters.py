'''Given a string s, find the length of the longest substring without duplicate characters.
 '''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        hashMap = {}
        for r in range(len(s)):                         # iterate over the string
            if s[r] in hashMap and hashMap[s[r]] >= l:  
                l = hashMap[s[r]] + 1                   # move `l` past the duplicate character
            hashMap[s[r]] = r                           # store/update last seen index of character
            count = max(count, r - l + 1)               # update max substring length

        return count

mySol = Solution()
s = "dvdf"
print(mySol.lengthOfLongestSubstring(s))
# print(mySol.lengthOfLongestSubstring(s = "ababcde"))
# print(mySol.lengthOfLongestSubstring(s = "pwwkew"))
# print(mySol.lengthOfLongestSubstring(s = ""))
# print(mySol.lengthOfLongestSubstring(s = "aA"))
# print(mySol.lengthOfLongestSubstring(s = "bbbbb"))
# print(mySol.lengthOfLongestSubstring(s = "abcdef"))