class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Add letter from word one, add letter from word two. 
        # Repeat until one exhaust
        # In case one exhaust, add the remaining letters of the other

        length1, length2 = len(word1), len(word2)
        min_length = min(length1, length2)

        merged_word = ""

        for i in range(min_length):
            merged_word += word1[i] + word2[i]

        difference = length1 - length2
        if difference > 0:
            merged_word += word1[-difference:]
        elif difference < 0:
            merged_word += word2[difference:]
            
        return merged_word
        



