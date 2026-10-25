'''
    每日温度
'''

class Solution:
    def dailyTemperatures(self, temperatures):
        # 单调栈
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
    