'''Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3'''

class Solution:
    def maxScore(self, s: str) -> int:
        l = len(s)                                      # calculate length of the string
        i = 0                                           # initialise a counter to keep track of indicies in the string
        x = 1                                           # initialise another counter to keep track of the split in the string
        max_s = 0                                       # initialise a variable to store max sum
        while i < l:
            zeros = s[:x].count('0')                    #count zeroes in LHS
            ones = s[x:].count('1')                     #count ones in RHS
            # print(f' 0 = {zeros}, 1 = {ones}, x = {x}')
            x += 1                                      # increment slicing counter
            t = zeros + ones 
            if t > max_s:                               # if zeroes in current LHS + ones in current RHS are the maximum then it would enter the if block and would be store in max_s
                # print(f't = {t}, max = {max_s}')
                max_s = t                               # store current max in max_s
            i += 1                                      # increment index counter
        return max_s                                    # return the max sum
    
mySol = Solution()
string = "11100"
print(mySol.maxScore(string))