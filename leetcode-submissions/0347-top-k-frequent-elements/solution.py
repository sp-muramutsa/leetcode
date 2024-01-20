class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        # Map each element with it's frequency
        element_frequency = {}
        for element in nums:
            if element not in element_frequency:
                element_frequency[element] = 1
                    
            else:
                element_frequency[element] += 1
        
        # sort dictionary based on frequency
        element_frequency = dict(sorted(element_frequency.items(), key=lambda x:x[1], reverse=True))

        # return k first ones
        return list(element_frequency.keys())[:k]

    


        
        
