'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
'''

class Solution(object):
    def getNext(self, next, s):
        next[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        next = [0] * len(s)
        self.getNext(next, s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False
        
# test
s = "abcabcabcabc"
print(Solution.repeatedSubstringPattern(Solution(), s))