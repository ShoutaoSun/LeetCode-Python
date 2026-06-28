'''
    双指针 - 三数之和
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:  # 剪枝，如果当前数大于0，后面不可能有和为0的三元组
                break

            if i > 0 and nums[i] == nums[i - 1]:  # 去重
                continue
            
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                
                    # 去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    # 移动指针继续找
                    left += 1
                    right -= 1

                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
    
# test
nums = [-1, 0, 1, 2, -1, -4]
print(Solution.threeSum(Solution, nums))