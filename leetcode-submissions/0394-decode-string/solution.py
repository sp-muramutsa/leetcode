class Solution:
    def decodeString(self, s: str) -> str:
        # Create stack
        stack = []
        res = ""
        # Iterate over the string
        for i in range(len(s)):
            # If the string is not "]" add to the stack
            if s[i] != "]":
                stack.append(s[i])
            # If it is "]" we pop from the stack until we hit "[" and then get pop again to get the number
            else:
                word = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # We push this back to the stack to keep the order of nested brackets
                stack.append(word * int(num))
        return "".join(stack)
