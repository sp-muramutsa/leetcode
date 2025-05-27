# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        minHeap = []

        for l in lists:
            if l:
                heapq.heappush(minHeap, l)

        dummy = ListNode()
        curr = dummy

        while minHeap:
            node = heapq.heappop(minHeap)
            curr.next = node
            if node.next:
                heapq.heappush(minHeap, node.next)
            curr = curr.next

        return dummy.next

