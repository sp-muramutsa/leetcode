# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return 
        i = 0
        dummy = head
        curr = dummy
        while curr:
            curr = curr.next
            i += 1
        if i == 1:
            return 
        position = i - n
        pointer2 = dummy
        for i in range(position-1):
            pointer2 = pointer2.next
        if position == 0:
            return pointer2.next
        pointer2.next = pointer2.next.next
        return dummy
