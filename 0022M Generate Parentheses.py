'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        validParenthesis = []                               # Stores all valid parenthesis combinations

        def dfs(left: int, right: int, path: list[str]):    
            if len(path) == 2 * n:                          # Base condition: if the sequence is complete
                validParenthesis.append("".join(path))      # Convert list to string and store
                return 
            if left < n:                                    # Add '(' if the count of '(' is less than n
                path.append('(')                            # Add '(' to the current sequence
                dfs(left + 1, right, path)                  # Recur with incremented '(' count
                path.pop()                                  # Backtrack: remove last added '('
            
            if right < left:                                # Add ')' only if it does not exceed '(' count
                path.append(')')                            # Add ')' to the current sequence
                dfs(left, right + 1, path)                  # Recur with incremented ')' count
                path.pop()                                  # Backtrack: remove last added ')'
        
        dfs(0, 0, [])                                       # Start DFS with 0 '(' and 0 ')'
        return validParenthesis                             # Return the list of valid sequences

mySol = Solution()
n = 5
print(mySol.generateParenthesis(n))