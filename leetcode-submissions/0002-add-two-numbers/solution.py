# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        # Itearate over both linked lists
        # Keep a carrier
        # Add the current values of both nodes if they exist, else add 0
        # Update the carrier if necessary
        # Move the pointers
        dummy = ListNode(0)
        p = dummy
        p1 = l1
        p2 = l2
        carrier = 0
        while p1 or p2:
            n1 = p1.val if p1 else 0
            n2 = p2.val if p2 else 0
            tot = n1 + n2 + carrier
            if tot >= 10:
                stay = tot % 10 
                carrier = tot // 10
                p.next = ListNode(stay)
                p = p.next
            else:
                carrier = 0
                p.next = ListNode(tot)
                p = p.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if carrier != 0:
            p.next = ListNode(carrier)

        return dummy.next
        
