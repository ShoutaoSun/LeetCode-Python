'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        word = ''
        s += ' '

        for char in s:
            if char == ' ':
                if word != '':
                    words.append(word)
                    word = ''
                continue

            word += char

        words.reverse()
        return ' '.join(words)
        
# test
s = "the sky is blue"
print(Solution.reverseWords(Solution(), s))