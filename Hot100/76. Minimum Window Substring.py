'''
    子串 - 最小覆盖子串
'''

class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):  # 剪枝
            return ""
        
        # 统计 t 中每个字符的需求量
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        missing = len(t)  # 表示还缺多少个字符才能覆盖 t
        left = 0
        min_len = len(s) + 1
        ans = ""

        for right, ch in enumerate(s):
            if ch in need:  # 若当前字符是 t 中需要的
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1

            while missing == 0:  # 当全部满足时，尝试收缩左边界
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left: right + 1]

                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        missing += 1
                left += 1

        return ans

# test
s = "ADOBECODEBANC"
t = "ABC"
print(Solution.minWindow(Solution, s, t))