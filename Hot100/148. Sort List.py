'''
    排序链表
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getListLength(self, head):
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        return cnt

    def splitList(self, head, size):
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next

        if cur is None or cur.next is None:
            return None
            
        next_head = cur.next
        cur.next = None  # 断开 next_head 的前一个节点
        return next_head

    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()  # 创建哨兵节点

        while list1 and list2:
            if list2.val > list1.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2  # 拼接剩余链表，返回第一个为真的值，如果都为假则返回最后一个值
        while cur.next:
            cur = cur.next

        return dummy.next, cur

    def sortList(self, head):
        length = self.getListLength(head)
        dummy = ListNode(next=head)
        step = 1  # 步长
        while step < length:
            new_list_tail = dummy  # 新链表的末尾
            cur = dummy.next
            while cur:
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)
                head, tail = self.mergeTwoLists(head1, head2)
                new_list_tail.next = head
                new_list_tail = tail
            step *= 2
        return dummy.next
    