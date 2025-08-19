class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        words = [w for w in words if w != ""]
        return " ".join(reversed(words)).strip()

       

