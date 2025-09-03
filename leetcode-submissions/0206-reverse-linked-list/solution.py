# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using a list we can crete a new linked list
        # The time and space complexity becomes O(n)
        # You return the reversed list after making it a linked list
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        res.reverse()
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
