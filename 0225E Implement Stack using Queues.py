class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.queue2 = self.queue1.copy()
        self.queue2.reverse()

    def pop(self) -> int:
        for i in range(0, len(self.queue2), 1):
            if self.queue2[i]:
                self.queue1.pop(-1)
                return self.queue2.pop(i)

    def top(self) -> int:
        for i in self.queue2:
            if i:
                return i
            
    def empty(self) -> bool:
        if not self.queue2:
            return True
        else:
            return False


myStack = MyStack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack.pop())
myStack.push(4)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())