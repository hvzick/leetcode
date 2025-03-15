'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.'''

class MinStack:
    def __init__(self):
        self.stack = []                                 # Main stack to store all values
        self.minStack = []                              # Stack to keep track of the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)                          # Push value onto the main stack

        if self.minStack:                               # Check if minStack is not empty
            minVal = min(val, self.minStack[-1])        # Store the smaller value between val and current min
        else:
            minVal = val                                # If minStack is empty, val is the minimum

        self.minStack.append(minVal)                    # Push the new minimum value onto minStack
        return self.stack, self.minStack

    def pop(self) -> None:
        self.stack.pop()                                # Remove the top value from the main stack
        self.minStack.pop()                             # Remove the corresponding min value from minStack
        return self.stack, self.minStack

    def top(self) -> int:
        return self.stack[-1]                           # Return the top value from the main stack

    def getMin(self) -> int:
        return self.minStack[-1]                        # Return the top value from minStack, which is the minimum

obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())