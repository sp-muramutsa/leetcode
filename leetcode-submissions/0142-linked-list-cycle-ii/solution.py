# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = slow = head

        def hasCycle(fast, slow):
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return (True, fast)
            return (False, None)

        presence = hasCycle(fast, slow)

        if not presence[0]:
            return None

        slow = head
        fast = presence[1]
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

