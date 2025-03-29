# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Better way to perform this problem for O(1) space is using slow and fast pointers, once the fast pointer catches up with the slow then that means there is a cycle in our linked list.
        if head is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
