from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Space Complexity:
        Time Complexity: O(n * k)

        """

        n = len(strs)
        hashmap = defaultdict(list)

        for i in range(n):
            pattern = [0] * 26
            word = strs[i]
            m = len(word)
            for j in range(m):
                pattern[ord(word[j]) - ord('a')] += 1
            hashmap[tuple(pattern)].append(word)
            
        return list(hashmap.values())
            

                
