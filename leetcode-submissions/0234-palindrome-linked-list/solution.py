# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse(start):

    prev, curr = None, start
    while curr:
        temp_next = curr.next
        curr.next = prev

        prev = curr
        curr = temp_next

    return prev


def get_first_half_end(head):
    # Use a fast and slow pointer. slow += 1. fast += 2
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 1. Edge cases
        if not head or not head.next:
            return True

        # 2. Iterate up to the middle of the list
        first_half_end = get_first_half_end(head)

        # 3. Reverse the last part of the list
        second_half_head = reverse(first_half_end.next)

        # 4. Compare palindrome property the first part and the last part
        p1, p2 = head, second_half_head
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

