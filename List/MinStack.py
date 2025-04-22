class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        if self.length == 0:
            self.stack.append((val, val))
        else:
            last_min = self.stack[-1][1]
            if  last_min < val:
                self.stack.append((val, last_min))
            else:
                self.stack.append((val, val))
        self.length += 1
    def pop(self) -> None:
        self.stack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
# Efficient
class Solution:

    def __init__(self):
        self.stack = []
        self.min = None
        
    # Add an element to the top of Stack
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min = x
        elif x >= self.min:
            self.stack.append(x)
        else:
            self.stack.append(2*x-self.min)
            self.min = x
            

    # Remove the top element from the Stack
    def pop(self):
        if not self.stack:
            return
        y = self.stack.pop()
        if y < self.min:
            self.min = 2 * self.min - y
        if not self.stack:
            self.min = None
        
    # Returns top element of Stack
    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1] if self.stack[-1] >= self.min else self.min

    # Finds minimum element of Stack
    def getMin(self):
        return self.min if self.stack else -1
        