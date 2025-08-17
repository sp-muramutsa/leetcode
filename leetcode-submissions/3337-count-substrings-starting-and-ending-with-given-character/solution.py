class Solution:
    def countSubstrings(self, s: str, c: str) -> int:

        n = s.count(c)
        return (n ** 2 + n) // 2
      
