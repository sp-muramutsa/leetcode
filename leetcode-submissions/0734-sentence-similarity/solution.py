class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        length1 = len(sentence1)
        length2 = len(sentence2)

        if length1 != length2:
            return False
        
        def is_similar(word1, word2):
            if word1 == word2:
                return True
            
            elif [word1, word2] in similarPairs or [word2, word1] in similarPairs:
                return True
        
        for i in range(length1):
            for j in range(length2):
                if i == j:
                    if not is_similar(sentence1[i], sentence2[i]):
                        return False
        
        return True
                    
        
       
        

        
