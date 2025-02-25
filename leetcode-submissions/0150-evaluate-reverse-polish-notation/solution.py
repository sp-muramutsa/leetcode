class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i, n = 0, len(tokens)

        while i < n:
            if tokens[i] not in ("+", "-", "*", "/"):
                stack.append(int(tokens[i]))
            else:
                # Do the operation between the two elements on the top of the stack and put the result on top of the stack
                element_2 = stack.pop()
                element_1 = stack.pop()
                match tokens[i]:
                    case "+":
                        new_result = element_1 + element_2
                    case "-":
                        new_result = element_1 - element_2
                    case "*":
                        new_result = element_1 * element_2
                    case "/":
                        new_result = int(
                            element_1 / element_2
                        )  # This is an important trick to round to 0 everytime in Python! Java and C++ and most other languages round to 0 by default.
                stack.append(new_result)
            i += 1

        return stack[0]

