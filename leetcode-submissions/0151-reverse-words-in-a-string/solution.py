class Solution:
    def reverseWords(self, s: str) -> str:
        substrings = s.split()
        merged_string = ""
        substrings = list(substrings)
        length = len(substrings)

        i = length 
        while i > 0:
            merged_string = merged_string + substrings[i - 1] + " "
            i -= 1
        
        return merged_string.rstrip()
        
