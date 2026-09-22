'''
    环形链表 II
'''

class Solution(object):
    def detectCycle(self, head):  # Floyd 判圈算法
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                   slow = slow.next
                   head = head.next
                return slow
        return None 
