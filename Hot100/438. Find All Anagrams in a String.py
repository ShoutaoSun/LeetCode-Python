'''
    滑动窗口 - 找到字符串中所有字母异位词
'''

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):  # 剪枝
            return []
        
        p_cnt = {}
        for p_str in p:
            p_cnt[p_str] = p_cnt.get(p_str, 0) + 1
        
        window_cnt = {}
        result = []

        for i in range(len(p)):
            ch = s[i]
            window_cnt[ch] = window_cnt.get(ch, 0) + 1
        
        if window_cnt == p_cnt:
            result.append(0)

        for i in range(len(p), len(s)):
            left_ch = s[i - len(p)]
            window_cnt[left_ch] -= 1
            if window_cnt[left_ch] == 0:
                del window_cnt[left_ch]
            
            right_ch = s[i]
            window_cnt[right_ch] = window_cnt.get(right_ch, 0) + 1

            if window_cnt == p_cnt:
                result.append(i - len(p) + 1)

        return result
    
# test
s = "cbaebabacd"
p = "abc"
print(Solution.findAnagrams(Solution, s, p))