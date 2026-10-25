'''
    有效的括号
'''

class Solution:
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if s[i] == ')' and stack[-1] == '(' or s[i] == ']' and stack[-1] == '[' or s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s[i])
        return not stack
