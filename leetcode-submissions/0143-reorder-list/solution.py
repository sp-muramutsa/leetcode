# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #We find the mid node using slow and fast pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        #We detach the first and second node
        slow.next = None
        #we reverse the second node
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        #we reorder the linked list
        while second:
            temp1, temp2 = head.next, second.next
            head.next = second
            second.next = temp1
            head = temp1
            second = temp2
