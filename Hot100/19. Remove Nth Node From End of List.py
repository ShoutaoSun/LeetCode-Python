'''
    删除链表的倒数第 N 个结点
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):  # 快慢指针，一趟扫描
        dummy = ListNode()
        dummy.next = head

        fast = slow = dummy
        for _ in range(n + 1):  # 快指针先走 n+1 步
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next