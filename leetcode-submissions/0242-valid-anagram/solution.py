class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
        for j in range(len(t)):
            hash_t[t[j]] = hash_t.get(t[j], 0) + 1
        for item in hash_s:
            if hash_s[item] != hash_t.get(item, 0):
                return False
        return True
        
