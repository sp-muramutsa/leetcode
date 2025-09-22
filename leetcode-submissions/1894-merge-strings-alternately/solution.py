class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create a result list 
        # A count if odd add word if even add word2
        # Iterate over the string if all indices aren't at the end
        # Afer iterating over both strings, check if all pointers are at the end
        # if not add the rest
        res = []
        count = 1
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if count % 2 != 0:
                res.append(word1[p1])
                p1 += 1
                count += 1
                continue

            if count % 2 == 0:
                res.append(word2[p2])
                p2 += 1
                count += 1
                continue

        if p1 < len(word1):
            for i in range(p1, len(word1)):
                res.append(word1[i])

        if p2 < len(word2):
            for j in range(p2, len(word2)):
                res.append(word2[j])

        return "".join(res)
