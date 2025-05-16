class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            if i in closing_brackets:
                if stack:
                    bracket = stack.pop()
                    if bracket != closing_brackets[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False

