# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getKth(self, curr, k):
        temp = curr

        for _ in range(k):
            if temp:
                temp = temp.next

        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # Reverse
            prev, curr = None, groupPrev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect the linked list
            tail = groupPrev.next
            groupPrev.next = kth
            tail.next = groupNext
            groupPrev = tail

        return dummy.next

