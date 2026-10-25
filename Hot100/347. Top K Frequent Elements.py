'''
    前 K 个高频元素
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # 统计每个元素的出现次数
        cnt = Counter(nums)
        max_cnt = max(cnt.values())

        # 把出现次数相同的元素，放到同一个桶中
        buckets = [[] for _ in range(max_cnt + 1)]
        for x, c in cnt.items():
            buckets[c].append(x)

        # 倒序遍历桶，把前 k 大的元素加入答案
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans

# test
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution.topKFrequent(Solution, nums, k))
