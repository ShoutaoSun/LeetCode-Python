'''
    链表 - 反转链表
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre