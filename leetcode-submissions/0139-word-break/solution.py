class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Iterative DP

        dictionary = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for start in range(n):
            for word in dictionary:
                end = start + len(word)

                if end > n + 1:
                    continue

                if dp[start] and word == s[start:end]:
                    dp[end] = True

        return dp[-1]

