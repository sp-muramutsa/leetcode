class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Manacher's Algorithm O(n)

        n = len(s)

        # Transform string
        t = "^#"
        for char in s:
            t += char + "#"
        t += "$"

        n = len(t)
        radii = [0] * n
        c = r = 0

        for i in range(1, n):

            # i is within r: Use mirror before expanding
            if i <= r:
                mirror = 2 * c - i
                radii[i] = min(radii[mirror], r - i)

            # i is beyond r: Expand
            left = i - radii[i] - 1
            right = i + radii[i] + 1

            while left >= 0 and right < n and t[left] == t[right]:
                radii[i] += 1
                left -= 1
                right += 1

            # Current palindrome is longer than previous one
            if i + radii[i] > r:
                r = i + radii[i]
                c = i

        max_radius = max(radii)
        max_center = radii.index(max_radius)

        start = (max_center - max_radius) // 2

        return s[start : start + max_radius]

