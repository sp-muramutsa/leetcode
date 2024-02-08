class Solution:
    def isPalindrome(self, s: str) -> bool:

        # upper to lower and remove non alphanums
        s = s.lower()
        length = len(s)
        new_s = ""

        for i in range(length):
            if s[i].isalnum():
                new_s += s[i]
        
        
        length_s = len(new_s)
        i = 0
        j = length_s - 1
        while i < length_s and j > 0:
            if new_s[i] == new_s[j]:
                pass
            else:
                return False
            i += 1
            j -= 1 
        
        return True
        
        
