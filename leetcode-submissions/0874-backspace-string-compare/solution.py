class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(word):
            result = []
            for char in word:
                if char == "#" and result:
                    result.pop()
                elif char != "#":
                    result.append(char)
    
            return ''.join(result)
    
        if backspace(s) == backspace(t):
            return True
        else:
            return False
    

    
        
