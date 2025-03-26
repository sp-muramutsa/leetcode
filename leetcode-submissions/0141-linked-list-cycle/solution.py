# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        hashmap = set() 
        
        curr = head
        while curr:
            if curr in hashmap:  
                return True
            hashmap.add(curr)  
            curr = curr.next  
        
        return False  
