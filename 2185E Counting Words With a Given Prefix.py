'''You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.'''

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        for i in words:                 # loop over the words in the list
            if i.startswith(pref):      # if the current word starts with the given prefix
                count += 1              # increment the count
        return count

mySol = Solution()
words = ["pay","attention","practice","attend"]
prefix = "at"
print(mySol.prefixCount(words, prefix))