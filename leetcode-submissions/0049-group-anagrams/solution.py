class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            sorted_word = sorted(i)
            hashmap[tuple(sorted_word)].append(i)
        return list(hashmap.values())
