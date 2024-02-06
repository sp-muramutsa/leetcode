class Solution:
    def removeStars(self, s: str) -> str:
        unstarred_s = []

        for i in s:
            if i == "*" and unstarred_s:
                unstarred_s.pop()
            elif i != "*":
                unstarred_s.append(i)
        
        return "".join(unstarred_s)

        
