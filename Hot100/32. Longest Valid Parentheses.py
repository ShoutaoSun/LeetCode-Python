'''
    最长有效括号
'''

class Solution:
    def longestValidParentheses(self, s):
        stack = []
        tmp = [0] * len(s)
        ans = 0
        cur = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    tmp[i] = tmp[j] = 1

        for num in tmp:
            if num:
                cur += 1
            else:
                ans = max(cur, ans)
                cur = 0
        ans = max(cur, ans)
        return ans

# test
s = "(()"
print(Solution.longestValidParentheses(Solution, s))
