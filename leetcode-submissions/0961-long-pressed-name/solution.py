from collections import Counter
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # If the length of typed is less than name return False
        # Using two pointers one for name another for typed we will move both
        # If the letters don' match return False
        # Move the typed letter until it doesn't match the current letter
        
        if len(typed) < len(name):
            return False
        
        p1, p2 = 0, 0
        
        while p2 < len(typed):
            if p1 < len(name) and name[p1] == typed[p2]:
                p1 += 1 
                p2 += 1
            elif p2 > 0 and typed[p2] == typed[p2 - 1]:
                p2 += 1
            else:
                return False
            
        return p1 == len(name)
