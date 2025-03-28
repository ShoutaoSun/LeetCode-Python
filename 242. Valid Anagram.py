'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: true
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for j in t:
            record[ord(j) - ord('a')] -= 1
        for val in record:
            if val != 0:
                return False
        return True

# test
s = 'anagram'
t = 'nagaram'
print(Solution.isAnagram(Solution(), s, t))