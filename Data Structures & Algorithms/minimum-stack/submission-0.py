class MinStack:
    stack = []
    mini = []

    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val: int) -> None:
        curr_min = self.mini[-1] if len(self.mini) else val
        self.mini.append(min(val, curr_min))
        self.stack.append(val)

    def pop(self) -> None:
        self.mini.pop()
        return self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
