class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        n = len(s)
        i = n - 1
        prev = 0
        curr = 0
        integer_val = 0

        while i > -1:
            curr = romans[s[i]]
            if curr < prev:
                integer_val -= curr
            else:
                integer_val += curr
            prev = curr
            i -= 1
        
        return integer_val


        
