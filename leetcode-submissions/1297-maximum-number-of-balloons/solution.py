class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in balloon_count: 
                balloon_count[char] += 1
            
        occurences = list(balloon_count.values())

        for number in occurences:
            if number < 1:
                return 0
        
        for number in occurences[2:4]:
            if number < 2:
                return 0

        ones = occurences[:2]
        ones.append(occurences[4]) 
        twos = occurences[2:4]


        result_ones = min(ones)
        result_twos = min(twos) // 2
        result = min(result_ones, result_twos)
    
       
        return result
        
