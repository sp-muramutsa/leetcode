from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            pattern = [0] * 26

            for char in word:
                pattern[ord(char) - ord('a')] += 1
            
            hashmap[str(pattern)].append(word) 
        
        return list(hashmap.values())
