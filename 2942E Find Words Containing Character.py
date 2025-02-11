'''You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.'''

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        c = []
        n = len(words)
        for i in range(0, n):
            if x in words[i]:
                c.append(i)
        return c

mySol = Solution()
words = ["leet","code"]
x = "e"
print(mySol.findWordsContaining(words, x))