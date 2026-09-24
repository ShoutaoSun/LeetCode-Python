'''
    随机链表的复制
'''

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        # 复制并插入新节点
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 分离链表
        tail = dummy = Node(0, head)
        cur = head
        while cur:
            copy = cur.next
            tail.next = copy
            cur.next = copy.next
            cur = cur.next
            tail = tail.next
        return dummy.next
        