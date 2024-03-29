from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """

        occurences = Counter(arr)
        hashset = set()
        
        for occurence in occurences.values():
            if occurence in hashset:
                return False
            else:
                hashset.add(occurence)
        
        return True

        
        
