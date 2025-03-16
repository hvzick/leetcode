'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":                # if digits is empty
            return []                   # return empty list
        digit_to_letters = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x', 'y','z'],
        }
        result = []
        def dfs(index: int, path: list[str]):
            if index == len(digits):                        # base case
                result.append("".join(path))                # append the result
                return                                      # return to previous stack
            for letter in digit_to_letters[digits[index]]:
                path.append(letter)                         # choose a letter
                dfs(index + 1, path)                        # recurse for next digit
                path.pop()                                  # backtrack (undo last choice)
        dfs(0, [])
        return result

mySol = Solution()
digits = '23'
print(mySol.letterCombinations(digits))