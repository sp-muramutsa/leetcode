class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        left, right = 0, len(needle)-1
        while right <= len(haystack)-1:
            if haystack[left:right+1] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1
