# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        # Move fast n steps
        for i in range(n):
            fast = fast.next

        # Move both pointers till fast is at the tail. slow will be at n.
        prev = slow
        while fast is not None:
            prev = slow
            slow = slow.next
            fast = fast.next

        # Remove nth node and return
        if slow.next:
            prev.next = slow.next
        else:
            prev.next = None

        return dummy.next

