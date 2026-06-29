'''
    滑动窗口 - 无重复字符的最长子串
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        last_index = {}  # 借助字典存储
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1
            
            last_index[ch] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
# test
s = "abcabcbb"
print(Solution.lengthOfLongestSubstring(Solution, s))
