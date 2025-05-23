'''
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example:
Input: s = "abbaca"
Output: "ca"
'''

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for str in s:
            if stack:
                if str == stack[-1]:
                    stack.pop()
                else:
                    stack.append(str)
            else:
                stack.append(str)
        return ''.join(stack)    

# test
s = "abbaca"
print(Solution.removeDuplicates(Solution(), s))