from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Intuition: See comments.
        """

        # Make permutations using a hashtable. Pretty smart.

        hashtable = Counter(s1)
        length1, length2 = len(s1), len(s2)
        l, r = (
            0,
            length1,
        )  # Move a window of size length1 accross s2 and check if the current substring in the window is a permutation of s1

        while r <= length2:
            if Counter(s2[l:r]) == hashtable:
                return True
            r += 1
            l += 1

        return False

