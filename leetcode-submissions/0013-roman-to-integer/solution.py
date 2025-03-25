class Solution:
    def romanToInt(self, s: str) -> int:
        # Symbol       Value
        #   I             1
        #   V             5
        #   X             10
        #   L             50
        #   C             100
        #   D             500
        #   M             1000
        res = 0
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if hashmap[s[i]] < hashmap[s[i+1]]:
                    val = hashmap[s[i+1]] - hashmap[s[i]]
                    res += val
                    i += 2
                else:
                    res += hashmap[s[i]]
                    i += 1
            else:
                res += hashmap[s[i]]
                i += 1
        return res

