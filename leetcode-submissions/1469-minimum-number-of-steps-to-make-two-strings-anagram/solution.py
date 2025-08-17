class Solution:
    def minSteps(self, s: str, t: str) -> int:

        n = len(s)

        hashmap_s = {chr(i): 0 for i in range(ord("a"), ord("a") + 26)}
        hashmap_t = {chr(i): 0 for i in range(ord("a"), ord("a") + 26)}

        for i in range(n):
            hashmap_s[s[i]] += 1
            hashmap_t[t[i]] += 1

        steps = 0
        for char in hashmap_t:
            if hashmap_s[char] > hashmap_t[char]:
                steps += abs(hashmap_s[char] - hashmap_t[char])

        return steps

