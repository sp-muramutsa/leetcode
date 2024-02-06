class Solution:
    def removeDuplicates(self, s: str) -> str:
        x = []

        for char in s:
            if x and char == x[-1]:
                x.pop()
            
            else:
                x.append(char)
        
        return "".join(x)



        

        
