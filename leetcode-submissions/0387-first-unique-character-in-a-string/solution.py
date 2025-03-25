class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Using just a hashmap
        hashmap = Counter(s)
        for i in s:
            if hashmap[i] == 1:
                return s.index(i)
        return -1
