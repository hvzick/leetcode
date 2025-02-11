class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        x = len(l[-1])
        return x

mySol = Solution()
s = "Hello World        "
print(mySol.lengthOfLastWord(s.strip()))