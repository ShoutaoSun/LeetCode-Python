'''
    回溯算法练习 - 分割问题
'''

class Solution(object):
    def partition(self, s):
        '''
        递归用于纵向遍历，for 循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到了一种方法
        '''
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, startIndex, path, result):
        # 递归终止条件
        if startIndex == len(s):
            result.append(path[:])
            return 
        
        # 单层递归逻辑
        for i in range(startIndex, len(s)):
            if self.is_palindrome(s, startIndex, i):
                path.append(s[startIndex:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def is_palindrome(self, s, start, end):
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# test
s = "aab"
print(Solution.partition(Solution(), s))