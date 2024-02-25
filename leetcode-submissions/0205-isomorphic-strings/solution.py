class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_hashmap = {}
        t_hashmap = {}

        length_s = len(s)
        length_t = len(t)

        for i in range(length_s):
            if s[i] not in s_hashmap:
                s_hashmap[s[i]] = [i]
            else:
                s_hashmap[s[i]].append(i)

        for j in range(length_t):
            if t[j] not in t_hashmap:
                t_hashmap[t[j]] = [j]
            else:
                t_hashmap[t[j]].append(j)
        
        return list(s_hashmap.values()) == list(t_hashmap.values())
