'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.'''

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split(" ")             # convert string list into the list
        new = l[:k]                  # store the modified list 
        return " ".join(new)         # convert the modified list into the string and return it

mySol = Solution()
s = "Hello how are you Contestant"
k = 4
print(mySol.truncateSentence(s, k))