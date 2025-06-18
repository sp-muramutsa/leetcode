class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{" 
        }
        stack = []
        for i in s:
            if i in hashmap:
                if len(stack) != 0:
                    if stack.pop() != hashmap[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True
            
