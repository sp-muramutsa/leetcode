class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dups = set()
        ans = 0
        for r in s:
            while r in dups:
                dups.remove(s[l])
                l += 1
            dups.add(r)
            ans = max(len(dups), ans)
        return ans

