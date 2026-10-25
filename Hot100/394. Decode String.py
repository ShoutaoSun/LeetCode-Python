'''
    字符串解码
'''

class Solution(object):
    def decodeString(self, s):
        stack = []
        res = ''
        k = 0

        for c in s:
            if c.isalpha():
                res += c
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((res, k))
                res = ''
                k = 0
            else:
                sub_res = res
                res, k = stack.pop()
                res += sub_res * k
                k = 0
        return res
