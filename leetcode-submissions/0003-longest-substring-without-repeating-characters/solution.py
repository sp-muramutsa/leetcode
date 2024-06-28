class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        Intuition: Slide a window through the string while enlarging it by unique characters. When you meet a character you already added, start afresh with your set. Update the longest substring as you go.
        """

        length = len(s)

        if length <= 1:
            return length

        l, r = 0, 0
        seen = set()
        longest = 0
        count = 0

        while r < length:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                l += 1
                r = l
                seen = set()
            longest = max(longest, len(seen))

        return longest

