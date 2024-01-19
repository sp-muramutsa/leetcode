class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Add letter from word one, add letter from word two. 
        # Repeat until one exhaust
        # In case one exhaust, add the remaining letters of the other

        length1 = len(word1)
        length2 = len(word2)

        max = length1

        if length2 > length1:
            max = length2
        

        merged_string = ""
        i = 0
        while i < max:
            try:
                merged_string += word1[i] + word2[i]
            except IndexError:
                break
            i += 1
        
        merged_string = merged_string + word1[i:] + word2[i:]

        return merged_string

