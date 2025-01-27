class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}

        for s in word1:
            hashmap_1[s] = hashmap_1.get(s, 0) + 1
        for t in word2:
            hashmap_2[t] = hashmap_2.get(t, 0) + 1
        
        for l in hashmap_1:
            if (hashmap_1.get(l, 0) - hashmap_2.get(l, 0)) > 3:
                return False
        for t in hashmap_2:
            if (hashmap_2.get(t, 0) - hashmap_1.get(t, 0)) > 3:
                return False

        return True
