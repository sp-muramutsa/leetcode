class Solution:
    def countSubstrings(self, s: str) -> int:

        # 3: Expanding from the centers: O(n ** 2) time and O(n) space

        n = len(s)
        palindromes = n

        for c in range(n):
            l, r = c - 1, c + 1
            while l >= 0 and r < n and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

        for c1 in range(n - 1):
            c2 = c1 + 1
            if s[c1] == s[c2]:
                palindromes += 1

                l, r = c1 - 1, c2 + 1

                while l >= 0 and r < n and s[l] == s[r]:
                    palindromes += 1
                    l -= 1
                    r += 1

        return palindromes

