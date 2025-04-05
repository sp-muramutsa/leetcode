class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hashset = set()
        answer = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            answer = max(answer, len(hashset))
        
        return answer
