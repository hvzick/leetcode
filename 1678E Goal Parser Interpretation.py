'''You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.'''

class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i in range(0, len(command)):
            if command[i] == 'G':                               # G -> G
                s += 'G'
            elif command[i] == '(' and command[i+1] == ')':     # () -> o
                s += 'o'
            elif command[i] == '(' and command[i+1] == 'a':     # (al) -> al
                s += 'al'
        return s

mySol = Solution()
command = "G()(al)"
print(mySol.interpret(command))