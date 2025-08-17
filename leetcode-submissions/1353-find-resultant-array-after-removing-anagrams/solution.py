class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        n = len(words)
        result = []

        def get_pattern(word):
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord('a')] += 1
            return pattern

        i = 0
        while i < n:
            curr = words[i]
            result.append(curr)
            curr_pattern = get_pattern(curr)
            
            while i < n and curr_pattern == get_pattern(words[i]):
                i += 1
        
        return result
