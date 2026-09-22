'''
    两数相加
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0  # 表示进位
        cur = dummy = ListNode()

        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            cur.next = ListNode(s % 10)  # 每个节点保存一个数位
            carry = s // 10  # 新的进位
            cur = cur.next
        return dummy.next  # 虚拟头节点的下一个节点就是头节点
