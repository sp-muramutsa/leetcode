# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        
        curr = self.head
        i = 0
        random_node = curr.val

        while curr:
            p = random.randint(0, i)

            if p < 1:
                random_node = curr.val

            i += 1
            curr = curr.next
        
        return random_node

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
