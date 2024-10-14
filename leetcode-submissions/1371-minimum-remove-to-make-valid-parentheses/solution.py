class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
       # invalidity: either a surplus of "(" or ")"
       # First sweep: If extra ")", skip them
       # Second sweep: If extra "(", remove them

        result = []
        count = 0

        # First sweep: Remove extra ")"
        for char in s:
            if char == "(":
                result.append("(")
                count += 1
            elif char == ")" and count > 0:
                count -= 1
                result.append(")")
            elif char != ")":
                result.append(char)
        
        # Second sweep: Remove extra "("
        filtered = []
        for char in result[::-1]:
            if char == "(" and count > 0:
                count -= 1
            else:
                filtered.append(char)
        
        return "".join(char for char in filtered)[::-1]

    
    
