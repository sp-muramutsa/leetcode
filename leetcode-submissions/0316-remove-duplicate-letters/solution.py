class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #We create a stack and a set to view visited chars
        stack = []
        seen = set()
        counter = Counter(s)
        #We go over the char and decrrese their count
        for i in s:
        #Now we check if we can pop the char if we have a replacement if the char is lower than the on in the stack
            counter[i] -= 1
            if i in seen:
                continue
            
            while stack and stack[len(stack)-1] > i and counter[stack[len(stack)-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(i)
            seen.add(i)
        return "".join(stack)
