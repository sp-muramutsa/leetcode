class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Write your code here
        def get_hash(s):
            res = []
            for char in s:
                res.append(ord(char) - ord("a"))

            res.sort()
            return "".join(str(res))

        hashmap = {}

        for word in strs:
            hash_ = get_hash(word)
            if hash_ in hashmap:
                hashmap[hash_].append(word)
            else:
                hashmap[hash_] = [word]

        return list(hashmap.values())

