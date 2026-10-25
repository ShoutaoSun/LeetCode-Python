'''
    最小栈
'''

class MinStack:
    def __init__(self):
        self.st = []
        self.mn = float('inf')

    def push(self, value):
        self.st.append(value - self.mn)
        self.mn = min(self.mn, value)

    def pop(self):
        self.mn -= min(self.st.pop(), 0)

    def top(self):
        return self.mn + max(self.st[-1], 0)
        

    def getMin(self):
        return self.mn
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
