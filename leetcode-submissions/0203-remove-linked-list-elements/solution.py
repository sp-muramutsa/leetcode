# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val == val:
            head = head.next
        
        if head is None:
            return
            
        prev = head
        curr = head.next

        while curr is not None:
            print(prev.val if prev else None, curr.val)
            if curr.val == val:
                prev.next = curr.next             
            else:
                prev = curr
            curr = curr.next
            
        
        return head
