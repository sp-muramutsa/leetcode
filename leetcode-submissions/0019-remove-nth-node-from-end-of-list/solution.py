# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        slow = fast = dummy

        # Fast walks n steps
        for i in range(n):
            fast = fast.next

        # Both Slow and Fast walk till Fast reaches the end
        prev, slow = None, slow
        while fast is not None:
            fast = fast.next
            prev = slow
            slow = slow.next

        # Now we know Slow is n steps from the end of the list: We can remove the node Slow
        prev.next = slow.next

        return dummy.next

