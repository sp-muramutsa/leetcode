class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Intuition: Set two pointers going from left to right in both strings. Check to see if a character in t is equal to s. If yes then increment the pointer in s. Increment the one in t everytime. At the end we check if all characters in s were found in t. This will work since it's a forward movement so the order of characters is maintained.
        """
        pointer_s = pointer_t = 0
        length_s = len(s)
        length_t = len(t)

        while pointer_t < length_t and pointer_s < length_s:
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        return pointer_s == length_s

        
        
