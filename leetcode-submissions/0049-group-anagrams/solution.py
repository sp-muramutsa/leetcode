from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Space Complexity: O(n * m)
        Time Complexity: O(n * m log m)
        """

        hashmap = defaultdict(list)

        for word in strs:
            alphabet_pattern = [0] * 26
            for char in word:
                alphabet_pattern[ord(char) - ord('a')] += 1
            
            key = tuple(alphabet_pattern)
            hashmap[key].append(word)
        
        return hashmap.values()
        
 
