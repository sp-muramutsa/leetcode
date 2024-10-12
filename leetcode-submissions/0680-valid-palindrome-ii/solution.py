class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        We use two pointers to iterate. One from the start and another from the end. We move the pointers whenever the characters are equal i.e. satisfies the property of palindrome. 
        We check for cases where it's not a palindrome and see if it would be a palindrome upon deletion of either the left pointed character or the right pointed one.
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
    
       
