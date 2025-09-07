# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            prev, curr = None, node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        l1_rev = rev(l1)
        l2_rev = rev(l2)
        p1 = l1_rev
        p2 = l2_rev
        
        counter = 0
        dummy = ListNode(0)
        p3 = dummy
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            tot = v1 + v2 + counter

            if tot>=10:
                p3.next = ListNode(tot%10)
                counter = tot//10
            else:
                p3.next = ListNode(tot)
                counter = 0
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            p3 = p3.next
        if counter > 0:
            p3.next = ListNode(counter)
        
        return rev(dummy.next)
