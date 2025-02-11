class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        open_p = ['(', '{', '[']
        close_p = [')', '}', ']']
        stk = []
        for i in range(0, len(s)):
            if s[i] in open_p:
                stk.append(s[i])
            elif s[i] in close_p:
                if not stk:
                    return False
                if s[i] == close_p[0] and stk[-1] == open_p[0]:
                    stk.pop()
                elif s[i] == close_p[1] and stk[-1] == open_p[1]:
                    stk.pop()
                elif s[i] == close_p[2] and stk[-1] == open_p[2]:
                    stk.pop()
                else:
                    return False
        if not stk:
            return True
        else:
            return False

mySol = Solution()
parenthesis = "){"
print(mySol.isValid(parenthesis))