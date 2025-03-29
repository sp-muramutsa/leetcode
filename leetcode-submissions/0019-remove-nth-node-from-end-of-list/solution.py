# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we first get the lenght of the linked list
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        #we get the position of the node
        position = count - n
        #we get the node before the node to be removed
        first = head
        for i in range(position-1):
            first = first.next
        #we check the Edge case
        if position == 0:
            return first.next
        #we skip the node to be removed
        first.next = first.next.next
        return head
