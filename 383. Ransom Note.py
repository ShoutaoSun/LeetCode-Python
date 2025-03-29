'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example:
Input: ransomNote = "a", magazine = "b"
Output: false
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        random = [0] * 26
        
        for i in magazine:
            random[ord(i) - ord('a')] += 1
        for j in ransomNote:
            random[ord(j) - ord('a')] -= 1
        return all(val >= 0 for val in random)

# test
ransomNote = "aa"
magazine = "aab"
print(Solution.canConstruct(Solution(), ransomNote, magazine))