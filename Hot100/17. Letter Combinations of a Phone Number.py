'''
    电话号码的字母组合
'''

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        
        ans = []
        path = [''] * n

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)

        dfs(0)
        return ans

# test
digits = "23"
print(Solution.letterCombinations(Solution, digits))
