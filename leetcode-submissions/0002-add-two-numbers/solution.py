# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p1 = dummy
        holder = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            total = d1 + d2 + holder
            holder = total // 10
            total = total % 10
            p1.next = ListNode(total)
            p1 = p1.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if holder > 0:
            p1.next = ListNode(holder)
        
        return dummy.next

