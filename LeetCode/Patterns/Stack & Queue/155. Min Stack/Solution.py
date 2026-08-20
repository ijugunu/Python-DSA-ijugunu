class MinStack:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, value: int) -> None:
        if len(self.st1)==0:
            self.st1.append(value)
            self.st2.append(value)
        else:
            mini=min(value,self.st2[-1])
            self.st1.append(value)
            self.st2.append(mini)           

    def pop(self) -> None:
        if len(self.st1)==0:
            return None
        self.st1.pop()
        self.st2.pop()
        return None   
        

    def top(self) -> int:
        if len(self.st1)==0:
            return None
        return self.st1[-1] 

    def getMin(self) -> int:
        if len(self.st1)==0:
            return None
        return self.st2[-1]    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()