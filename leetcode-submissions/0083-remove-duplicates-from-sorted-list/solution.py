# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(val=float("-inf"))
        dummy.next = head

        prev, curr = dummy, head

        while curr is not None:
            if prev.val == curr.val:
                temp_next = curr.next
                prev.next = temp_next
                curr = temp_next
            else:
                prev = curr
                curr = curr.next

        return dummy.next

