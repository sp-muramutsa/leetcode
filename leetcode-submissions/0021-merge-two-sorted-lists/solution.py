# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case if one or both are empty return the one which is not empty
        # Create a dummy node
        # Create pointer for dummy
        # Create pointers for both nodes
        # While both p1 and p2 are not None
        # Point the node to the smallest and move the pointer with smallest

        dummy = ListNode(0)
        p1 = dummy
        p2 = list1
        p3 = list2
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        while p2 and p3:
            if p2.val > p3.val:
                p1.next = p3
                p3 = p3.next
            else:
                p1.next = p2
                p2 = p2.next
            p1 = p1.next

        if p2:
            p1.next = p2
        
        if p3:
            p1.next = p3

        return dummy.next

