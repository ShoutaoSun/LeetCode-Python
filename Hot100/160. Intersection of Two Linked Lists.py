'''
    链表 - 相交链表
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB

        while pA != pB:
            if pA != None:
                pA = pA.next
            else:
                pA = headB

            if pB != None:
                pB = pB.next
            else:
                pB = headA

        return pA