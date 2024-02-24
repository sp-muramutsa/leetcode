class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_list = list(s.split(" "))
        pattern_count = len(pattern)
        s_count = s.count(" ") + 1
        
        
        pattern_hashmap = {}
        s_hashmap = {}

        for i in range(pattern_count): 
            if pattern[i] not in pattern_hashmap:
                pattern_hashmap[pattern[i]] = [i]
            else:
                pattern_hashmap[pattern[i]].append(i)
        
        for j in range(s_count):
            if s_list[j] not in s_hashmap:
                s_hashmap[s_list[j]] = [j]
            else:
                s_hashmap[s_list[j]].append(j)
       
        
        print(pattern_hashmap)
        print(s_hashmap)
        
        return list(pattern_hashmap.values()) == list(s_hashmap.values())
        
        

       

        




        

        
