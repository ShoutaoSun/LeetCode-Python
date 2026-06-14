'''
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i+1][j-1] + 2

        return dp[0][-1]

# test
s = 'bbbab'
print(Solution.longestPalindromeSubseq(Solution(), s))