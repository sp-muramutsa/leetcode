from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        length_s =  len(s)
        length_t =  len(t)

        if length_s != length_t:
            return False

        s_hashmap = defaultdict(list)
        for i in range(length_s):
            s_hashmap[s[i]].append(i)
        
        t_hashmap = defaultdict(list)
        for j in range(length_t):
            t_hashmap[t[j]].append(j)
        
        return list(s_hashmap.values())== list(t_hashmap.values()) 
