'''
    合并两个有序链表
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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
        return dummy.next