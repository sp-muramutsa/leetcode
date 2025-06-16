class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        hashmap1, hashmap2 = {}, {}
        n = len(pattern)
        
        if n != len(s_list):
            return False
        
        for i in range(n):
            hashmap1[pattern[i]] = s_list[i]
            hashmap2[s_list[i]] = pattern[i]
        
      
        for i in range(n):
            if hashmap1[pattern[i]] != s_list[i]:
                return False
            elif hashmap2[s_list[i]] != pattern[i]:
                return False
            
        return True
    

        
        return True
