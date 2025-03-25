class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        if s[0] in hashmap:
            return False
        for i in s:
            if i in hashmap and stack:
                end_string = stack.pop()
                if end_string != hashmap[i]:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
