class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self. min_stack.append(val)
        else:
            if self.stack[-1]<=self.min_stack[-1]:
                self. min_stack.append(val)
        
    def pop(self) -> None:
        pop=self. stack.pop()
        if pop==self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()