'''There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.'''

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0                               # initialise X to 0
        for i in operations:                # loop over the operations
            if i == "--X" or i == "X--":    # check if current operations is --X or X--
                x -= 1                      # decrement 1 from x
            else:                           # when current operation is X++ or ++X
                x += 1                      # increment 1 to x
        return x                            # return X

mySol = Solution()
operations = ["--X","X++","X++"]
print(mySol.finalValueAfterOperations(operations))