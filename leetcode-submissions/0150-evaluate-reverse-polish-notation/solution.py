class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def addition(a, b):
            return int(a + b)
        def subtraction(a, b):
            return int(a - b)
        def multiplication(a, b):
            return int(a * b)
        def division(a, b):
            return int(a / b)
        hashmap = {
            "+": addition,
            "-": subtraction,
            "*": multiplication,
            "/": division
        }
        # we create our stack
        stack = []
        for i in tokens:
            if i in hashmap and stack:
                b = stack.pop()
                a = stack.pop()
                f = hashmap[i]
                stack.append(f(a,b))
            else:
                stack.append(int(i))
        return stack[0]
