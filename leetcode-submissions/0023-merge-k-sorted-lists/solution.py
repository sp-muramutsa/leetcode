# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, HeapNode(head))

        dummy = ListNode(val=float("-inf"))
        curr = dummy

        while min_heap:
            smallest = heapq.heappop(min_heap)
            node = smallest.node
            curr.next = node

            if node.next:
                heapq.heappush(min_heap, HeapNode(node.next))

            curr = curr.next

        return dummy.next

