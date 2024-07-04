class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = len(s)
        l, r = 0, 0
        max_freq = 0
        longest = 0
        hashmap = {chr(i): 0 for i in range(65, 91)}

        while r < length:
            hashmap[s[r]] += 1
            window_size = r - l + 1
            max_freq = max(max_freq, hashmap[s[r]])

            if window_size - max_freq <= k:
                longest = max(longest, window_size)

            else:
                hashmap[s[l]] -= 1
                l += 1

            r += 1

        return longest

