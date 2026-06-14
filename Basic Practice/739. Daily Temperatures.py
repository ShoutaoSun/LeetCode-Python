'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)  # 单调栈存放的是数组元素的对应下标
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
    
        return result
        
# test
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution.dailyTemperatures(Solution(), temperatures))