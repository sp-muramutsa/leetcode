# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            curr = head
            prev = None

            while curr is not None:
                temp_next = curr.next
                curr.next = prev
                prev, curr = curr, temp_next

            return prev

        # Reverse the list
        newHead = reverse(head)

        # Iterate through the reversed list, removing elements whose superiors we have seen

        dummy = ListNode(0)
        dummy.next = newHead

        maximum = float("-inf")
        prev, curr = dummy, newHead

        while curr is not None:
            if curr.val < maximum:
                prev.next = curr.next
            else:
                maximum = curr.val
                prev = curr
            curr = curr.next

        # Reverse again
        resultHead = reverse(dummy.next)
        return resultHead

