from typing import List


class Solution:

    def manacher_radii(self, s: str) -> List[int]:

        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        radii = [0] * n

        center, radius = 0, 0

        for right in range(1, n - 1):
            if radius > right:
                mirror = 2 * center - right
                radii[right] = min(radius - right, radii[mirror])

            while t[right + (1 + radii[right])] == t[right - (1 + radii[right])]:
                radii[right] += 1

            if right + radii[right] > radius:
                center, radius = right, right + radii[right]

        return radii

    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1 or len(s) == 0:
            return s

        radii = self.manacher_radii(s)
        print(radii)

        # Get max length and center
        max_radius = max(radii)
        max_center = radii.index(max_radius)

        # Compute start in original string
        start = (max_center - max_radius) // 2
        return s[start : start + max_radius]

