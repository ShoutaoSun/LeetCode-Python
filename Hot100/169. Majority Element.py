'''
    多数元素
'''

class Solution:
    def majorityElement(self, nums):
        ans = hp = 0
        for num in nums:
            if hp == 0:
                ans, hp = num, 1  # 初始擂主生命值为 1
            else:
                hp += 1 if num == ans else -1
        return ans

# test
nums = [2,2,1,1,1,2,2]
print(Solution.majorityElement(Solution, nums))
