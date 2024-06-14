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
    
        return backspace(s) == backspace(t)
 
    

    
        

    
        
