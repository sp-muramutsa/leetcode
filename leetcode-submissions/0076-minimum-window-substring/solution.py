from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counter = Counter(t)
        window_counter = {char: 0 for char in t_counter}

        need, have = len(t_counter), 0
        l, r, n = 0, 0, len(s)
        min_window, min_length = "", float("inf")

        while r < n:
            r_char = s[r]
            if r_char in t_counter:
                window_counter[r_char] += 1
                if window_counter[r_char] == t_counter[r_char]:
                    have += 1

            # Valid window
            while have == need:
                curr_window = s[l : r + 1]

                if len(curr_window) < min_length:
                    min_window = curr_window
                    min_length = len(curr_window)

                # Shrink the window from the left
                l_char = s[l]
                if l_char in t_counter:
                    window_counter[l_char] -= 1

                    if window_counter[l_char] < t_counter[l_char]:
                        have -= 1
                l += 1

            r += 1

        return min_window

