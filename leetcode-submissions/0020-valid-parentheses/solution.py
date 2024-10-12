class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")" : "(", "}": "{", "]": "["}

        stack = []
        n = len(s)
        i = 0

        while i < n:
            # opening bracket: push it to the top of the stack
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            # closing bracket: check if the top of the stack is its opening if yes, pop. else, return false.
            else:
                if stack and hashmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

            i += 1
           
        return not stack



