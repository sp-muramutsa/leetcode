class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        n = len(s)
        count = 0
        prev, curr = 0, 1

        for i in range(1, n):
            if s[i-1] != s[i]:
                count += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        
        count += min(prev, curr)
        
        return count 

        
