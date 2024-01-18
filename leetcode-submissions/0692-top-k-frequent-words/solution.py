class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = {}
        for word in words:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        
        
        frequencies = sorted(frequencies.items(), key=lambda x:(-x[1], x[0]))
        frequencies = dict(frequencies)
        
        frequent_words = list(frequencies.keys())
        
        return frequent_words[:k]
       

        

        
        


        
