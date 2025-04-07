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