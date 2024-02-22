class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """ 
        Time O(n)
        Space O(n)
        """
        length = len(s)
        if length <= 10:
            return []
    
        sequences = set()
        repeated_sequences = set()
    
        i = 0
        j = 10
    
        while j <= length:
            substring = s[i:j]
            if substring in sequences:
               repeated_sequences.add(substring)
            else:
               sequences.add(substring)
        
            i += 1
            j += 1
    
        return list(repeated_sequences)

        
         
