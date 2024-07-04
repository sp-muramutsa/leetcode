class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Time: O(n)
        Space: O(n)

        Intuition:
        Use a stack to keep track of the valid scores. Iterate through the list of operations, and for each operation:
        - If the operation is an integer, convert it to an int and push it onto the stack.
        - If the operation is "+", calculate the sum of the top two elements in the stack and push the result onto the stack.
        - If the operation is "D", double the top element in the stack and push the result onto the stack.
        - If the operation is "C", pop the top element from the stack (invalidate the most recent score).

        After processing all operations, the sum of the stack will be the total score.
        """

        stack = []

        for char in operations:

            top = int(stack[-1]) if stack else None
            penultimate = int(stack[-2]) if len(stack) >= 2 else None
            
            try:
                char = int(char)   
                stack.append(char)
            except ValueError:
                pass 
            
            if char == "+":
                stack.append(top + penultimate)
            
            elif char == "D":
                stack.append(2 * top) 

            elif char == "C":
                stack.pop()      
        
        return sum(stack)


        
