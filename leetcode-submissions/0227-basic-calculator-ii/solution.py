class Solution:
    def calculate(self, s: str) -> int:
        # Using the BODMAS
        # Bracket Order Division Multiplication Addition Subtraction
        #5
        #[3]
        s = s.replace(" ", "")
        length = len(s)
        if length == 0:
            return 0
        
        num = 0
        i = 0
        stack = []
        op = '+'

        while i < length:
            curr = s[i]

            if curr.isdigit():
                num = num * 10 + ord(curr) - ord('0')

            if (not curr.isdigit()) or i == length - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    temp = stack.pop()
                    stack.append(int(temp/num))
                op = curr
                num = 0
            i += 1
        return sum(stack)
            

