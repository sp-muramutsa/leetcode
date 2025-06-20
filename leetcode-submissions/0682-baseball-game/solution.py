class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #x record new score
        #+ record sum of previous 2 scores
        #D record double of the previous score
        #C remove the previous score
        # ["5","2","C","D","+"] [5, 10, 15]  30
        #       ^

        # Create a stack
        stack = []
        # We iterate over the ops
        for i in range(len(operations)):
            # If it is part of those functionalties we operate and record the result
            if operations[i] == "+":
                tot = stack[-1] + stack[-2]
                stack.append(tot)
            
            elif operations[i] == "D":
                double = stack[-1] * 2
                stack.append(double)
            
            elif operations[i] == "C":
                stack.pop()
            
            else:
                stack.append(int(operations[i]))
        return sum(stack)
