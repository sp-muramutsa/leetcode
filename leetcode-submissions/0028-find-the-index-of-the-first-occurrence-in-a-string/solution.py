class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case if neddle is less than haystack return -1
        # Create a window for needle
        # While right of neddle is less than the lenght of haystack
        # Check if neddle equals the haystack in the window if yes return the left
        # Return the -1
        if len(needle) > len(haystack):
            return -1

        l, r = 0, len(needle)
        print(haystack[l:r])
        while r < len(haystack)+1:
            if needle == haystack[l:r]:
                return l
            r += 1
            l += 1

        return -1
