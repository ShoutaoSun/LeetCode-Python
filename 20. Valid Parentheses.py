'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
 
Example:
Input: s = "()"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif not stack or item != stack[-1]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True