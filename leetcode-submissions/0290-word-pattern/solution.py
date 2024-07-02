from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_hashmap = defaultdict(list)
        i = 0
        length_pattern = len(pattern)
        for i in range(length_pattern):
            pattern_hashmap[pattern[i]].append(i)
       
        s_hashmap = defaultdict(list)
        j = 0
        s_list = s.split(" ")
        length_s = len(s_list)
        for j in range(length_s):
            s_hashmap[s_list[j]].append(j)
        
        return list(pattern_hashmap.values()) == list(s_hashmap.values())
       
        

        

