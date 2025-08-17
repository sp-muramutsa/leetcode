class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord("a")] += 1
            anagrams[tuple(pattern)].append(word)

        return list(anagrams.values())

