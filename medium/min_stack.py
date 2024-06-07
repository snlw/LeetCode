# https://leetcode.com/problems/min-stack/submissions/1280106624/

# Type: Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = 2**32 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValue = min(self.minValue, val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minValue:
            if len(self.stack) > 0:
                self.minValue = min(self.stack)
            else:
                self.minValue = 2**32 

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minValue
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
