'''
    链表 - 回文链表
'''

class Solution(object):
    def middleNode(self, head):  # 寻找中间节点，快慢指针法
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):  # 反转链表
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head):  # 包含复原链表
        mid = self.middleNode(head)
        head2 = h2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        self.reverseList(h2)  # 复原
        return True
    