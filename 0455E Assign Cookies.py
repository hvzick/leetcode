class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        print(g)
        print(s)
        count = 0
        i = 0 
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count
    
mySol = Solution()
g = [10,9,8,7]
s = [5,6,7,8]
print(mySol.findContentChildren(g, s))