class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """


        n = len(s)
        if n <= 1:
            return s
        stack = [s[0]]
        

        for i in range(1, n):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(char for char in stack)
        


        
        
