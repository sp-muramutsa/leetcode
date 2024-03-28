class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabets = {letter : 0 for letter in range(97, 123)}

        for char in sentence:
            ascii_code = ord(char)
            alphabets[ascii_code] += 1
    
        
        return min(alphabets.values()) > 0
        
