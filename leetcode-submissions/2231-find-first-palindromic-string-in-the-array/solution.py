class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):
            return s == s[::-1]

        
        for word in words:
            if is_palindrome(word):
                return word
        
        return ""
        
