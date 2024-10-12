class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_alpha = ""

        for char in s:
            if char.isalnum():
                s_alpha += char.lower()

        
        i, j = 0, len(s_alpha) - 1

        while i <= j:
            if s_alpha[i] != s_alpha[j]:
                return False
            i += 1
            j -= 1
        return True
        
