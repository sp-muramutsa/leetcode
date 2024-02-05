class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if i not in s[:s.index(i)] + s[s.index(i) + 1: ]:
                return s.index(i)
        return -1
        
