'''You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.'''

import math  # Importing math module for rounding operations

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        postFixStack = []                               # Stack to store operands and intermediate results

        for i in range(0, len(tokens)):                 # Loop through each token in the input list
            if self.is_integer(tokens[i]):              # Check if the token is an integer
                postFixStack.append(int(tokens[i]))     # Convert to int and push onto the stack
            else:
                if len(postFixStack) > 1:               # Ensure at least two numbers are in the stack for operation
                    b = postFixStack.pop()              # Pop the top operand (right operand)
                    a = postFixStack.pop()              # Pop the next operand (left operand)
                    if tokens[i] == '+':  
                        c = a + b                       # Perform addition
                    elif tokens[i] == '-':  
                        c = a - b                       # Perform subtraction
                    elif tokens[i] == '*':  
                        c = a * b                       # Perform multiplication
                    elif tokens[i] == '/':  
                        c = a / b
                    postFixStack.append(int(c))         # Push the result back onto the stack
                    # print(postFixStack)               # Debugging statement
        return postFixStack[0]                          # Return the final result (single value left in stack)
    def is_integer(self, s):  
        try:
            int(s)  # Try converting the string to an integer
            return True  # If successful, it's an integer
        except ValueError:
            return False  # If conversion fails, it's not an integer

mySol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(mySol.evalRPN(tokens))