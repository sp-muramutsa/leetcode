class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        Time: O(n) where n in the length of t
        Space: O(1)
        Intuition:
        Use two pointers to traverse both strings. The idea is to check if all characters of `s` appear in `t` in the same order.
        - Initialize two pointers: `s_pointer` for string `s` and `t_pointer` for string `t`.
        - Traverse `t` with `t_pointer` and whenever a character in `t` matches the current character in `s` (pointed to by `s_pointer`), move the `s_pointer` to the next character.
        - If `s_pointer` reaches the end of `s`, it means all characters of `s` have been found in `t` in the correct order, so return True.
        - If the loop finishes and `s_pointer` has not reached the end of `s`, return False.
        
        """

        s_pointer, t_pointer = 0, 0
        s_length, t_length = len(s), len(t)

        while s_pointer < s_length and t_pointer < t_length:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1  
        
        if s_pointer == s_length:
            return True
        else:
            return False
    


       
        
        


