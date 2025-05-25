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

        # 1. Find the middle element
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. Reverse the second part
        prev, curr = None, slow

        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next

        # 3. Merge the two lists
        p1, p2 = head, prev

        while p2.next:
            temp_next_1 = p1.next
            p1.next = p2
            p1 = temp_next_1

            temp_next_2 = p2.next
            p2.next = temp_next_1
            p2 = temp_next_2

