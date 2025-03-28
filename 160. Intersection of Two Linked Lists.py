'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
- intersectVal: The value of the node where the intersection occurs. This is 0 if there is no intersected node.
- listA: The first linked list.
- listB: The second linked list.
- skipA: The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
- skipB: The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        
        # curB points the list with more elements
        curA, curB = headA, headB
        if lenA > lenB:
            curA, curB = headB, headA
        l = (lenB - lenA) if lenB > lenA else (lenA - lenB)
        for _ in range(l):
            curB = curB.next
        while lenA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
            lenA -= 1
        return None