class Solution:
    def validPalindrome(self, s: str) -> bool:

        """
        Time O(n)
        Space O(n^2)
   
        The intuition is we try to remove the right or left pointer and then check if the
        remaining string would be a palindrome, was the pointer removed. But we only do that
        in cases where left and right are different so we save time
        """   

        left, right= 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left+1 : right+1]
                skip_right = s[left : right]

                return (skip_left == skip_left[::-1] or 
                        skip_right == skip_right[::-1])

            left += 1
            right -= 1
            
        
        return True
                    

        
