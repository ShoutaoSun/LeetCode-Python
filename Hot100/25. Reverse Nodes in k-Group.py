'''
    K 个一组翻转链表
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        last_tail = dummy = ListNode(0, head)  # last_tail 是上一组翻转后的尾结点

        # k 个一组处理
        while True:
            cur = last_tail
            for _ in range(k):
                cur = cur.next
                if cur is None:  # 不足 k 个结点
                    return dummy.next

            pre = None
            cur = last_tail.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            tail = last_tail.next
            tail.next = cur
            last_tail.next = pre
            last_tail = tail
