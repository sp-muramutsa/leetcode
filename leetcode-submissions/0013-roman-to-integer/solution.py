class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I" :      1,
            "V" :       5,
            "X" :       10,
            "L" :       50,
            "C" :       100,
            "D" :       500,
            "M" :       1000
        }
        tot = 0
        i = 0
        while i < len(s):
            if i <= (len(s) - 2) and hashmap[s[i]] < hashmap[s[i+1]]:
                tot += hashmap[s[i+1]] - hashmap[s[i]]
                i += 2
            else:
                tot += hashmap[s[i]]
                i += 1
        return tot
