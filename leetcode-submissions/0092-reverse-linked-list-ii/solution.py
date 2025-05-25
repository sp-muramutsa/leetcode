# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        beforeLeft, curr = dummy, head
        for i in range(left - 1):
            beforeLeft, curr = beforeLeft.next, curr.next

        prev = None
        for j in range(left, right + 1):
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next

        beforeLeft.next.next = curr
        beforeLeft.next = prev

        return dummy.next

