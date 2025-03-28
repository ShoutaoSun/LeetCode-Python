'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create dummy head nodes to simplify the deletion process
        dummy_head = ListNode(next = head)

        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
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

arr = [1, 2, 6, 3, 4, 5, 6]
val = 6
arr_lst = create_list(arr)
print(linked_list_to_list(Solution.removeElements(Solution(), arr_lst, val)))