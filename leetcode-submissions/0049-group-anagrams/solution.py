from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap where key is the tuple of asci value of the word and value is a list of group anagrams
        # Iterate over the list
        # Create a key using the array oof 26 letters where each index represents count of a letter
        # If the key is in hashmap add the string to the array 
        hashmap = defaultdict(list)
        def get_key(string):
            chars = [0] * 26
            for i in string:
                num = ord(i) - ord("a")
                chars[num] += 1

            return tuple(chars)

        for i in strs:
            key = get_key(i)
            hashmap[key].append(i)
        res = []
        for i in hashmap:
            res.append(hashmap[i])
        return res

