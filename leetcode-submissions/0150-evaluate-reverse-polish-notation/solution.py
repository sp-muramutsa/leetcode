class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def multiply(x, y):
            return x * y
        def subtract(x, y):
            return y - x
        def add(x, y):
            return x + y
        def divide(x, y):
            return int(y / x)  
        
        hashmap = {
            '*': multiply,
            '-': subtract,
            '+': add,
            '/': divide
        }
        
        for i in tokens:
            if i in hashmap:
                val_1 = int(stack.pop()) 
                val_2 = int(stack.pop())
                new_val = hashmap[i](val_1, val_2)
                stack.append(str(new_val))
            else:
                stack.append(i)
        
        return int(stack[0]) 
