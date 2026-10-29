'''
    寻找重复数
'''

class Solution:
    def findDuplicate(self, nums):  # 环形链表思想
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]  # 等价于 fast = fast.next.next
            if fast == slow:  # 快慢指针移动到同一个节点
                break

        head = 0  # 再用一个指针，从起点出发
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        return slow  # 入环口即重复元素
