class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        l, r = 0, len(needle) - 1
        while r <= len(haystack) - 1:
            if haystack[l:r+1] == needle:
                return l
            else:
                l += 1
                r += 1
        return -1
