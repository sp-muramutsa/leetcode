class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # The logic here is to remove to keep the smaller numbers at the front and removing the larger ones
        # Create a stack that store numbers
        stack = []
        # Iterate over the stack if the number is smaller than the last digit of our stack we pop from our stack until we've removed all numbers larger to keep the stack monotonic.
        for i in num:
            # If the number of k is reached we return the answer
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(i)
        # After the iteration and we still have k we pop from the stack and return the stack
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        res = "".join(stack).lstrip("0")
        return res if res else "0"
