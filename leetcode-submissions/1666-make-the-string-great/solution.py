class Solution:
    def makeGood(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)
        Intuition: Iterate while checking to see if the letter on the top of the stack is the lowercase/uppercase version of our current letter. If yes, get rid of both letters i.e. pop the stack and don't append the current letter. If no, push the current letter on the stack.
        """

        length = len(s)
        stack = [s[0]]

        for i in range(1, length):
            if s[i].islower():
                if stack and stack[-1] == s[i].upper():
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                if stack and stack[-1] == s[i].lower():
                    stack.pop()
                else:
                    stack.append(s[i])

        return "".join(char for char in stack)

