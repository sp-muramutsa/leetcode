class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        """

        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        merged_string = ""
        a, b = 0, 0


        while a < n:
            merged_string += word1[a] + word2[a] 
            a += 1

        difference = abs(n1 - n2)
        if difference > 0:
            merged_string += (word1[-difference:] if n1 > n2 else word2[-difference:])
        return merged_string 



