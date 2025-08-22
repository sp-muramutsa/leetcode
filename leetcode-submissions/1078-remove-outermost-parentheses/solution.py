class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Create a stack
        # Create a result list
        # Iterate over the string
        # If the string is closing bracket pop from th stack
        # If stack is empty don't add th string to the result
        # Add the string to the stack and result
        
        stack = []
        result = []
        
        for i in s:
            if i == ")":
                stack.pop()
                
                if len(stack) == 0:
                    continue
                    
                result.append(i)
                
            else:
                if len(stack) == 0:
                    stack.append(i)
                    continue
                stack.append(i)
                result.append(i)
                
        return "".join(result)
