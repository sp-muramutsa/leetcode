class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Intuition:
        Use a two-pointer technique to check characters from the beginning and the end.
        If characters mismatch, check the substrings formed by skipping one character
        from either end. If any of those substrings is a palindrome, the original string
        can be a palindrome by removing one character.
        """


        length = len(s)
        l, r = 0, length - 1

        
        while l < r:
            if s[l] != s[r]:
                left_s = s[:l] + s[l+1:]
                right_s = s[:r] + s[r+1:]
                return left_s == left_s[::-1] or right_s == right_s[::-1]
            l += 1
            r -= 1
     
        
        return True
    
       
