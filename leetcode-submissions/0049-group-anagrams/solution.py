class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # empty hashmap

        # iterate
        # hash a word
        # if we find a word with the same characters, we add it to the word's list of words
        # return the dictionaries's values

        hashmap = {}

        for word in strs: # O(n)
            sorted_word = "".join(sorted(word)) # for word of length m: O(mlogm)
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else:
                 hashmap[sorted_word].append(word)
        
        return list(hashmap.values())

        # Time complexity: n + n * (mlogm) --> O(mlogm)

        
        
