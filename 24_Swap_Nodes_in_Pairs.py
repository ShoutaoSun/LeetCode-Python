'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next != None and cur.next.next != None:
            tmp1 = cur.next
            tmp2 = cur.next.next.next
            cur.next = cur.next.next
            tmp1.next.next = tmp1
            tmp1.next = tmp2
            cur = cur.next.next
        return dummy_head.next
        
# test
def create_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

head = [1, 2, 3, 4]
print(linked_list_to_list(Solution.swapPairs(Solution(), create_list(head))))