class Solution:
    def calculate(self, s: str) -> int:
        """
        Intuition: Store individual numbers, products, and quotients. Add them up at the end.
        Dangers: enumerate, parse properly, do an operation at the end, truncate towards 0, update operation and current number
        """
        # Initialize a stack to store what to be summed
        stack = []
        current_number = 0
        operation = '+'
        s = s.replace(" ", "")  # Remove any spaces in the string

        # Iterate over the string
        for i, char in enumerate(s):
            # Parse the digits into an int
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if not char.isdigit() or i == len(s) - 1: # You have to do an operation at the end
                # + or -: append a number or its inverse
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)

                # * or /: multiply or divide what's at the top of the stack
                elif operation == '*':
                    stack[-1] = stack[-1] * current_number
                elif operation == '/':
                    # Perform integer division (truncated towards zero)
                    stack[-1] = int(stack[-1] / current_number)
                
                # Update operation and reset current number
                operation = char
                current_number = 0
        
        # Return the sum of all values in the stack
        return sum(stack)
