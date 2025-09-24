class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        
        while start < end:
            temporary_string = s[start]
            
            s[start] = s[end]
            s[end] = temporary_string
            
            start += 1
            end -= 1
            

        
