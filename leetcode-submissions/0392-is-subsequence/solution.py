class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # fix a char in s
        # iterate t till we find the character. 
        # if we do. we fix the next character in s. and so on
        # if we don't find the s character in all of t we return false

        length_s = len(s)
        length_t = len(t)
       
        s_pointer = 0
        t_pointer = 0

        while t_pointer < length_t and s_pointer < length_s:
            checker = s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            else:
                pass
            t_pointer += 1
        
        return s_pointer == length_s

        """ 
        Time O(n + m)
        Space O(1)
        """

    


       
        
        


