class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for i in s1:
            hashmap[i] = hashmap.get(i, 0) + 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            count = Counter(s2[l:r+1])
            if count == hashmap:
                return True
            else:
                r += 1
                l += 1
        return False
