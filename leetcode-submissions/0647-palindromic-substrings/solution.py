class Solution:
    def countSubstrings(self, s: str) -> int:

        # 4: Manacher's Algorithm: Time O(n) and Space: O(n)

        m = len(s)
        palindromes = 0

        t = "^#" + "#".join(s) + "#$"

        n = len(t)
        radii_length = [0] * n
        center = right = 0

        for i in range(1, n - 1):

            # Mirror
            if i <= right:
                mirror = 2 * center - i
                radii_length[i] = min(radii_length[mirror], right - i)

            # Expand
            l = i - radii_length[i] - 1
            r = i + radii_length[i] + 1

            while l >= 0 and r < n and t[l] == t[r]:
                radii_length[i] += 1
                l -= 1
                r += 1

            # Found longer palindrome: Update right and center
            if i + radii_length[i] > right:
                right = i + radii_length[i]
                center = i

        return sum((radius + 1) // 2 for radius in radii_length)

