'''
    合并 K 个升序链表
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        cur = dummy = ListNode()

        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 or head2
        return dummy.next

    def mergeKLists(self, lists):  # 两两合并，自底向上
        m = len(lists)
        step = 1
        if m == 0:
            return None

        while step < m:
            for i in range(0, m - step, step * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + step])
            step *= 2
        return lists[0]
        