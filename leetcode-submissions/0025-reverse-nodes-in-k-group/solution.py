# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLinkedList(self, head, k):

        # First, check if there are at least k nodes
        temp = head
        for _ in range(k):
            if not temp:
                return -1
            temp = temp.next

        prev, curr = None, head
        newGroupHead = prev
        newGroupTail = head
        n = 0
        while curr and n < k:
            temp = curr.next

            if n == k - 1:
                newCurr = temp
            curr.next = prev
            prev = curr
            curr = temp
            n += 1

        newGroupHead = prev
        return (newGroupHead, newGroupTail, newCurr)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    

        dummy = ListNode(0, head)
        groupPrev = dummy
        curr = dummy.next

        while curr:
            # Reverse happened
            res = self.reverseLinkedList(curr, k)
            if res != -1:
                newHead, newTail, newCurr = res
                groupPrev.next = newHead
                groupPrev = newTail
                curr = newCurr

            else:
               break
        
       
        temp = dummy
        while temp.next:
            temp = temp.next
        temp.next = curr

        return dummy.next

