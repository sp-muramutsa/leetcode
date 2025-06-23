# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        res = ListNode(0)
        pointer = res
        # Reverse the list for both of them
        def reverse_lst(lst):
            curr = lst
            prev = None

            while curr:
                tmp = curr.next  
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        lst1 = reverse_lst(l1)
        lst2 = reverse_lst(l2)
        # Create a new list node
        divisor = 0
        # We move through the keep ading the values 
        while lst1 is not None or lst2 is not None:
        # If the number is grreater than 10 keep the remainder and store the divisor
            tot = divisor + (lst1.val if lst1 is not None else 0) + (lst2.val if lst2 is not None else 0)
            if tot >= 10:
                num = tot % 10
                divisor = tot // 10
            else:
                num = tot
                divisor = 0
            pointer.next = ListNode(num)
            pointer = pointer.next
            lst1 = (lst1.next if lst1 is not None else None)
            lst2 = (lst2.next if lst2 is not None else None)
        if divisor != 0:
            pointer.next = ListNode(divisor)
        return reverse_lst(res.next)
