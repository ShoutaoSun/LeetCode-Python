'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Example:
Input: ["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []]
Output: [null, null, null, 2, 2, false]
'''
from collections import deque

class MyStack(object):

    def __init__(self):
        self.que = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        tmp = self.que.popleft()
        self.que.append(tmp)
        return tmp
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que