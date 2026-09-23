'''
    两两交换链表中的节点
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        pre = dummy

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next

            pre.next = b
            a.next = b.next
            b.next = a

            pre = a
        return dummy.next
