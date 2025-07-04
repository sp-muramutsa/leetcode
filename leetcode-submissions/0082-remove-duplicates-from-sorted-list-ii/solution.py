# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(val=0, next=head)
        prev, curr = dummy, head

        while curr and curr.next:

            if curr.val == curr.next.val:
                
                value = curr.val
                while curr and curr.val == value:
                    curr = curr.next
                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next

