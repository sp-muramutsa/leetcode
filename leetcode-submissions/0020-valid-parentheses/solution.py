class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if stack and i in hashmap:
                if stack[-1] != hashmap[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
