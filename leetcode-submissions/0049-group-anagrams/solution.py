class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            pattern = [0] * 26
            for j in i:
                pattern[ord(j) - ord("a")] += 1
            hashmap[tuple(pattern)].append(i)
        res = []
        for i in hashmap.values():
            res.append(i)
        return res
