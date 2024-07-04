class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        Intuition: When you encounter an opening bracket, push it to the top of the stack. When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
        """

        
        length, stack = len(s), []
        open_to_close = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # Closing parenthesis
            if char in open_to_close: # For dictionary keys. Closing parentheses in this case.
                if stack and stack[-1] == open_to_close[char]:
                    stack.pop()
                else:
                    return False
            else: # Opening parentheses
                stack.append(char)
  
        return True if not stack else False
      
            
       
       

   
        
