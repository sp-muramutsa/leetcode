class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            pattern = [0] * 26
            for j in i:
                num = ord(j) - ord('a')
                pattern[num] += 1
            hashmap[tuple(pattern)].append(i)
        return list(hashmap.values())
