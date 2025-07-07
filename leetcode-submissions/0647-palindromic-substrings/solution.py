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

    def countSubstrings(self, s: str) -> int:

        radii = self.manacher_radii(s)

        palindromes = 0
        for radius in radii: 
            palindromes += (radius + 1) // 2
            
        return palindromes

