class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else :
                inner_score = stack.pop()
                outer_score = stack.pop()
                new_score = outer_score + max(1, inner_score*2)
                stack.append(new_score)

        return stack[0]


